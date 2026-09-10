# GoogleBand - Cyberpunk Music Creation App

## 🎵 Features

### Core Music Creation
- **128 MIDI Instruments** - Full General MIDI support
- **Keyboard** - 15-note piano keyboard (C3 to C5)
- **16-Step Sequencer** - Create drum and melody patterns
- **Pattern Recording** - Record and layer multiple patterns

### 🎙️ Recording & Playback
- **Audio Recording** - Record from microphone
- **MIDI Recording** - Capture note sequences
- **Real-time Playback** - Hear your music instantly
- **Multi-track Recording** - Layer multiple instruments

### ⚡ Audio Effects
- **Reverb** - Add spacious ambience
- **Echo/Delay** - Time-based effects
- **Distortion** - Aggressive tone shaping
- **Chorus** - Rich, modulated sound
- **Compressor** - Dynamic range control

### 🎨 Cyberpunk Neon Dark Theme
- Electric neon cyan, magenta, and purple accents
- Deep space black backgrounds
- Glowing button effects and animations
- Responsive mobile UI (optimized for phones)

### 💾 File Management
- Save recordings as WAV files
- Export patterns as MIDI
- Import MIDI files
- Auto-save functionality

---

## 🚀 Installation

### Android (via Buildozer)
```bash
buildozer android debug
```

### Development (Desktop)
```bash
pip install -r requirements.txt
python main.py
```

---

## 📱 UI Components

### Main Screen
- **Title** - "GOOGLEBAND CYBERPUNK MUSIC STUDIO"
- **Instrument Selector** - Choose from 128 MIDI instruments
- **Keyboard Section** - 15-note virtual keyboard
- **Sequencer** - 16-step pattern editor
- **Recording Controls** - Record/Stop/Save buttons
- **Effects Panel** - Apply real-time audio effects

### Color Scheme
| Element | Color | Hex | RGB |
|---------|-------|-----|-----|
| Background | Deep Black | #0a0e27 | 0.04, 0.055, 0.15 |
| Panels | Dark Blue | #1a1f3a | 0.06, 0.08, 0.1 |
| Primary Accent | Neon Cyan | #00ffff | 0, 1, 1 |
| Secondary Accent | Neon Magenta | #ff00ff | 1, 0, 1 |
| Highlight | Neon Pink | #ff1493 | 1, 0.08, 0.58 |

---

## 🎮 Usage

### Playing Notes
1. Select an instrument from the dropdown
2. Click keyboard keys to play notes
3. Adjust velocity and duration as needed

### Recording Audio
1. Click **● RECORD** to start
2. Play notes or sing into microphone
3. Click **⏹ STOP** when finished
4. Click **💾 SAVE** to store recording

### Creating Patterns
1. Open Sequencer
2. Select drum sound or instrument
3. Click steps (0-15) to add notes
4. Adjust BPM and time signature
5. Click Play to hear pattern

### Applying Effects
1. Select a recording or pattern
2. Click an effect button (Reverb, Echo, etc.)
3. Adjust effect parameters
4. Preview the result

---

## 🔧 Technical Details

### Audio Engine
- **PyAudio** - Microphone input/output
- **FluidSynth** - MIDI synthesis
- **SoundFont** - instruments.sf2 (31MB soundfont)

### MIDI Support
- 16 channels
- 128 instruments (General MIDI)
- Note velocity sensitivity
- Program change support

### File Formats
- **WAV** - Uncompressed audio recordings
- **MIDI** - Note sequences (.mid)
- **SF2** - SoundFont instrument definitions

---

## 📝 File Structure

```
googleband/
├── main.py                 # Main Kivy application
├── audio_recorder.py       # Recording & effects module
├── sequencer.py            # 16-step sequencer engine
├── cyberpunk_theme.py      # Theme & color configuration
├── server.py               # Flask web interface
├── buildozer.spec          # Android build config
├── instruments.sf2         # 31MB soundfont library
├── general.sf2             # General MIDI soundfont
└── recordings/             # Saved recordings directory
```

---

## 🎨 Customization

### Change Theme Colors
Edit `cyberpunk_theme.py`:
```python
CYBERPUNK_THEME = {
    'primary_bg': '#0a0e27',  # Change background color
    'neon_cyan': '#00ffff',   # Change accent colors
    ...
}
```

### Add New Effects
Extend `audio_recorder.py`:
```python
def apply_effect(self, effect_type, **params):
    if effect_type == 'my_effect':
        # Your effect code
```

### Create Custom Patterns
Use `sequencer.py`:
```python
sequencer = DrumSequencer(bpm=120)
sequencer.generate_common_pattern('rock')
```

---

## 🐛 Troubleshooting

### "No audio output"
- Ensure FluidSynth is installed: `apt-get install fluidsynth`
- Check soundfont files exist in project directory
- Verify microphone permissions on Android

### "MIDI notes not playing"
- Confirm instrument is selected
- Check velocity value (should be 0-127)
- Verify soundfont is valid

### "App crashes on recording"
- Grant microphone permissions
- Check available storage space
- Ensure PyAudio is properly installed

---

## 📄 License

This APK is free. Any reselling will be punishable by... well, you know.

---

## 🎵 Keep Creating!

Make amazing music with **GoogleBand** 🚀
