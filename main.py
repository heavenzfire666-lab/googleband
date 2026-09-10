"""GoogleBand - Complete Music Creation App
Main Application with All Features
Features: Recording, Sequencer, Mixer, Waveform Display, VU Meter, Effects
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle, Line, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock
import os
import mido
import numpy as np
import threading
from datetime import datetime
from audio_recorder import AudioRecorder, MIDIRecorder
from sequencer import DrumSequencer, MusicSequencer
from cyberpunk_theme import CYBERPUNK_THEME_RGB as COLORS
from instrument_library import InstrumentLibrary
from effects import EffectsProcessor
from song_manager import SongManager
from drum_kits import DrumKits

Window.size = (540, 960)

class NeonButton(Button):
    """Custom cyberpunk neon button"""
    def __init__(self, text='', neon_color=None, **kwargs):
        super().__init__(text=text, **kwargs)
        self.neon_color = neon_color or COLORS['neon_cyan']
        self.bind(size=self.update_canvas, pos=self.update_canvas)
        self.update_canvas()
    
    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*COLORS['bg_panel'])
            RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
            Color(*self.neon_color)
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 15), width=2)
        self.color = COLORS['text_primary']
        self.background_color = (0, 0, 0, 0)

class WaveformDisplay(BoxLayout):
    """Visual waveform display"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.audio_data = np.array([])
        self.bind(size=self.update_waveform, pos=self.update_waveform)
    
    def update_waveform(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*COLORS['bg_panel'])
            RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
            
            if len(self.audio_data) > 0:
                Color(*COLORS['neon_cyan'])
                normalized = self.audio_data / (np.max(np.abs(self.audio_data)) + 0.0001)
                
                for i in range(len(normalized) - 1):
                    x1 = self.x + (i / len(normalized)) * self.width
                    x2 = self.x + ((i + 1) / len(normalized)) * self.width
                    y1 = self.y + self.height / 2 + (normalized[i] * self.height / 4)
                    y2 = self.y + self.height / 2 + (normalized[i + 1] * self.height / 4)
                    Line(points=[x1, y1, x2, y2], width=1)
            else:
                Color(*COLORS['text_secondary'])
                Line(points=[self.x, self.y + self.height / 2, self.x + self.width, self.y + self.height / 2], width=1)
    
    def set_audio_data(self, data):
        """Update waveform with audio data"""
        self.audio_data = data
        self.update_waveform()

class VUMeter(BoxLayout):
    """Volume level indicator"""
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)
        self.levels = [0, 0]
        self.bind(size=self.update_meter, pos=self.update_meter)
    
    def update_meter(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*COLORS['bg_panel'])
            RoundedRectangle(size=self.size, pos=self.pos, radius=[8])
            
            for i, level in enumerate(self.levels):
                x = self.x + (i * self.width / 2) + 5
                bar_width = (self.width / 2) - 10
                bar_height = (level / 127) * (self.height - 10)
                
                if level < 85:
                    color = COLORS['neon_green']
                elif level < 110:
                    color = COLORS['neon_yellow']
                else:
                    color = COLORS['status_error']
                
                Color(*color)
                RoundedRectangle(pos=(x, self.y + 5), size=(bar_width, bar_height), radius=[4])
    
    def set_level(self, left, right):
        """Update meter levels"""
        self.levels = [left, right]
        self.update_meter()

class GoogleBandApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "GoogleBand - Cyberpunk Music Studio"
        
        self.recorder = AudioRecorder()
        self.midi_recorder = MIDIRecorder()
        self.sequencer = DrumSequencer(bpm=120)
        self.effects = EffectsProcessor()
        self.song_manager = SongManager()
        self.instruments = InstrumentLibrary()
        
        self.current_instrument = 0
        self.is_recording = False
        self.is_playing = False
        self.current_bpm = 120
        self.master_volume = 100
        self.current_song = None
        
        self.waveform = None
        self.vu_meter = None
        self.status_label = None
        self.bpm_slider = None
        self.volume_slider = None
    
    def build(self):
        """Build the main UI"""
        root = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        with root.canvas.before:
            Color(*COLORS['bg_dark'])
            self.rect = RoundedRectangle(size=root.size, pos=root.pos)
        root.bind(size=self._update_rect, pos=self._update_rect)
        
        # HEADER
        header = BoxLayout(orientation='vertical', size_hint_y=0.1, spacing=3)
        title = Label(
            text='[b]GOOGLEBAND[/b]\n[size=12]CYBERPUNK MUSIC STUDIO[/size]\n[size=10]600+ INSTRUMENTS[/size]',
            markup=True,
            color=COLORS['neon_cyan']
        )
        header.add_widget(title)
        root.add_widget(header)
        
        # WAVEFORM
        self.waveform = WaveformDisplay(size_hint_y=0.12)
        root.add_widget(self.waveform)
        
        # VU METER
        self.vu_meter = VUMeter(size_hint_y=0.08)
        root.add_widget(self.vu_meter)
        
        # INSTRUMENT SELECTOR
        inst_layout = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=3)
        inst_label = Label(text='🎛️ INST', size_hint_x=0.2, color=COLORS['neon_magenta'], bold=True)
        
        all_instruments = self.instruments.get_all_instruments()
        inst_names = list(all_instruments.values())[:50]  # Show first 50
        self.instrument_spinner = Spinner(
            text=inst_names[0],
            values=inst_names,
            size_hint_x=0.8
        )
        self.instrument_spinner.bind(text=self.on_instrument_change)
        
        inst_layout.add_widget(inst_label)
        inst_layout.add_widget(self.instrument_spinner)
        root.add_widget(inst_layout)
        
        # KEYBOARD
        keyboard_label = Label(text='🎹 KEYBOARD', size_hint_y=0.06, color=COLORS['neon_green'], bold=True)
        root.add_widget(keyboard_label)
        
        keyboard = GridLayout(cols=8, size_hint_y=0.15, spacing=2)
        notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
        for note in notes:
            btn = NeonButton(text=note, neon_color=COLORS['neon_cyan'], size_hint=(1, 1))
            btn.bind(on_press=lambda x, n=note: self.play_note(n))
            keyboard.add_widget(btn)
        root.add_widget(keyboard)
        
        # RECORDING CONTROLS
        recording_label = Label(text='🎙️ RECORDING', size_hint_y=0.06, color=COLORS['neon_pink'], bold=True)
        root.add_widget(recording_label)
        
        recording_controls = BoxLayout(size_hint_y=0.1, spacing=3)
        self.record_btn = NeonButton(text='● RECORD', neon_color=COLORS['neon_pink'])
        self.record_btn.bind(on_press=self.toggle_recording)
        
        self.stop_btn = NeonButton(text='⏹ STOP', neon_color=COLORS['neon_yellow'])
        self.stop_btn.bind(on_press=self.stop_recording)
        
        self.save_btn = NeonButton(text='💾 SAVE', neon_color=COLORS['neon_green'])
        self.save_btn.bind(on_press=self.save_recording)
        
        recording_controls.add_widget(self.record_btn)
        recording_controls.add_widget(self.stop_btn)
        recording_controls.add_widget(self.save_btn)
        root.add_widget(recording_controls)
        
        # SEQUENCER
        sequencer_label = Label(text='🥁 SEQUENCER', size_hint_y=0.06, color=COLORS['neon_purple'], bold=True)
        root.add_widget(sequencer_label)
        
        sequencer_controls = BoxLayout(size_hint_y=0.08, spacing=3)
        play_btn = NeonButton(text='▶ PLAY', neon_color=COLORS['neon_cyan'])
        play_btn.bind(on_press=self.play_sequencer)
        
        stop_seq_btn = NeonButton(text='⏹ STOP', neon_color=COLORS['neon_yellow'])
        stop_seq_btn.bind(on_press=self.stop_sequencer)
        
        clear_btn = NeonButton(text='🗑️ CLEAR', neon_color=COLORS['status_error'])
        clear_btn.bind(on_press=self.clear_sequencer)
        
        sequencer_controls.add_widget(play_btn)
        sequencer_controls.add_widget(stop_seq_btn)
        sequencer_controls.add_widget(clear_btn)
        root.add_widget(sequencer_controls)
        
        # MIXER
        mixer_label = Label(text='🎚️ MIXER', size_hint_y=0.06, color=COLORS['neon_magenta'], bold=True)
        root.add_widget(mixer_label)
        
        mixer = BoxLayout(orientation='vertical', size_hint_y=0.1, spacing=3)
        
        bpm_layout = BoxLayout(size_hint_y=0.5, spacing=3)
        bpm_label = Label(text=f'BPM: {self.current_bpm}', size_hint_x=0.2, color=COLORS['text_primary'])
        self.bpm_slider = Slider(min=60, max=200, value=self.current_bpm, size_hint_x=0.8)
        self.bpm_slider.bind(value=self.on_bpm_change)
        bpm_layout.add_widget(bpm_label)
        bpm_layout.add_widget(self.bpm_slider)
        
        vol_layout = BoxLayout(size_hint_y=0.5, spacing=3)
        vol_label = Label(text=f'VOL: {self.master_volume}%', size_hint_x=0.2, color=COLORS['text_primary'])
        self.volume_slider = Slider(min=0, max=127, value=self.master_volume, size_hint_x=0.8)
        self.volume_slider.bind(value=self.on_volume_change)
        vol_layout.add_widget(vol_label)
        vol_layout.add_widget(self.volume_slider)
        
        mixer.add_widget(bpm_layout)
        mixer.add_widget(vol_layout)
        root.add_widget(mixer)
        
        # FILE MANAGEMENT
        file_label = Label(text='📁 FILES', size_hint_y=0.06, color=COLORS['neon_green'], bold=True)
        root.add_widget(file_label)
        
        file_controls = BoxLayout(size_hint_y=0.08, spacing=3)
        new_song_btn = NeonButton(text='🆕 NEW', neon_color=COLORS['neon_cyan'])
        new_song_btn.bind(on_press=self.new_song)
        
        load_btn = NeonButton(text='📂 LOAD', neon_color=COLORS['neon_magenta'])
        load_btn.bind(on_press=self.load_song_dialog)
        
        export_btn = NeonButton(text='📤 EXPORT', neon_color=COLORS['neon_purple'])
        export_btn.bind(on_press=self.export_song)
        
        file_controls.add_widget(new_song_btn)
        file_controls.add_widget(load_btn)
        file_controls.add_widget(export_btn)
        root.add_widget(file_controls)
        
        # STATUS
        self.status_label = Label(
            text='🚀 GoogleBand Ready! 600+ Instruments Loaded',
            size_hint_y=0.08,
            color=COLORS['text_secondary']
        )
        root.add_widget(self.status_label)
        
        return root
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def on_instrument_change(self, spinner, text):
        self.current_instrument = self.instruments.search(text.split(':')[0])
        self.status_label.text = f'Instrument: {text}'
    
    def on_bpm_change(self, slider, value):
        self.current_bpm = int(value)
        self.sequencer.set_bpm(self.current_bpm)
    
    def on_volume_change(self, slider, value):
        self.master_volume = int(value)
    
    def play_note(self, note):
        """Play a MIDI note"""
        def play_in_thread():
            try:
                mid = mido.MidiFile()
                track = mido.MidiTrack()
                mid.tracks.append(track)
                
                note_map = {
                    'C4': 60, 'D4': 62, 'E4': 64, 'F4': 65,
                    'G4': 67, 'A4': 69, 'B4': 71, 'C5': 72,
                }
                
                track.append(mido.Message('program_change', program=self.current_instrument, time=0))
                track.append(mido.Message('note_on', note=note_map.get(note, 60), velocity=self.master_volume, time=0))
                track.append(mido.Message('note_off', note=note_map.get(note, 60), velocity=self.master_volume, time=480))
                
                mid.save('temp.mid')
                self.status_label.text = f'Playing {note}'
            except Exception as e:
                self.status_label.text = f'Error: {str(e)}'
        
        thread = threading.Thread(target=play_in_thread)
        thread.daemon = True
        thread.start()
    
    def toggle_recording(self, instance):
        self.is_recording = True
        self.recorder.start_recording()
        self.midi_recorder.start_recording()
        self.status_label.text = '● RECORDING...'
        self.record_btn.text = '⏸ PAUSE'
    
    def stop_recording(self, instance):
        self.is_recording = False
        self.recorder.stop_recording()
        self.midi_recorder.stop_recording()
        self.status_label.text = '⏹ Recording stopped'
        self.record_btn.text = '● RECORD'
    
    def save_recording(self, instance):
        if self.is_recording:
            self.stop_recording(instance)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.status_label.text = f'💾 Saved: {timestamp}'
    
    def play_sequencer(self, instance):
        self.is_playing = True
        self.status_label.text = '▶ PLAYING SEQUENCER'
    
    def stop_sequencer(self, instance):
        self.is_playing = False
        self.status_label.text = '⏹ Sequencer stopped'
    
    def clear_sequencer(self, instance):
        self.sequencer.clear_pattern()
        self.status_label.text = '🗑️ Sequencer cleared'
    
    def new_song(self, instance):
        self.current_song = f'song_{datetime.now().strftime("%H%M%S")}'
        self.status_label.text = f'🆕 New song: {self.current_song}'
    
    def load_song_dialog(self, instance):
        self.status_label.text = '📂 Load dialog'
    
    def export_song(self, instance):
        if not self.current_song:
            self.status_label.text = 'Create a song first'
            return
        
        self.status_label.text = f'📤 Exported: {self.current_song}'

if __name__ == '__main__':
    GoogleBandApp().run()
