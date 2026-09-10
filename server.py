from flask import Flask, render_template_string, request, send_file
import os
import mido

app = Flask(__name__)

NOTE_MAP = {
    'C3': 48, 'D3': 50, 'E3': 52, 'F3': 53, 'G3': 55, 'A3': 57, 'B3': 59,
    'C4': 60, 'D4': 62, 'E4': 64, 'F4': 65, 'G4': 67, 'A4': 69, 'B4': 71, 'C5': 72,
    'E2': 40, 'A2': 45, 'D3': 50, 'G3': 55, 'B3': 59
}

# All 128 Official General MIDI Instruments
GM_INSTRUMENTS = {
    # Piano
    0: "Acoustic Grand Piano", 1: "Bright Acoustic Piano", 2: "Electric Grand Piano", 3: "Honky-Tonk Piano",
    4: "Electric Piano 1", 5: "Electric Piano 2", 6: "Harpsichord", 7: "Clavinet",
    # Chromatic Percussion
    8: "Celesta", 9: "Glockenspiel", 10: "Music Box", 11: "Vibraphone",
    12: "Marimba", 13: "Xylophone", 14: "Tubular Bells", 15: "Dulcimer",
    # Organ
    16: "Drawbar Organ", 17: "Percussive Organ", 18: "Rock Organ", 19: "Church Organ",
    20: "Reed Organ", 21: "Accordion", 22: "Harmonica", 23: "Tango Accordion",
    # Guitar
    24: "Acoustic Guitar (nylon)", 25: "Acoustic Guitar (steel)", 26: "Electric Guitar (jazz)", 27: "Electric Guitar (clean)",
    28: "Electric Guitar (muted)", 29: "Overdriven Guitar", 30: "Distortion Guitar", 31: "Guitar harmonics",
    # Bass
    32: "Acoustic Bass", 33: "Electric Bass (finger)", 34: "Electric Bass (pick)", 35: "Fretless Bass",
    36: "Slap Bass 1", 37: "Slap Bass 2", 38: "Synth Bass 1", 39: "Synth Bass 2",
    # Strings
    40: "Violin", 41: "Viola", 42: "Cello", 43: "Contrabass",
    44: "Tremolo Strings", 45: "Pizzicato Strings", 46: "Orchestral Harp", 47: "Timpani",
    # Ensemble
    48: "String Ensemble 1", 49: "String Ensemble 2", 50: "SynthStrings 1", 51: "SynthStrings 2",
    52: "Choir Aahs", 53: "Voice Oohs", 54: "Synth Voice", 55: "Orchestra Hit",
    # Brass
    56: "Trumpet", 57: "Trombone", 58: "Tuba", 59: "Muted Trumpet",
    60: "French Horn", 61: "Brass Section", 62: "Synth Brass 1", 63: "Synth Brass 2",
    # Reed
    64: "Soprano Sax", 65: "Alto Sax", 66: "Tenor Sax", 67: "Baritone Sax",
    68: "Oboe", 69: "English Horn", 70: "Bassoon", 71: "Clarinet",
    # Pipe
    72: "Piccolo", 73: "Flute", 74: "Recorder", 75: "Pan Flute",
    76: "Blown Bottle", 77: "Shakuhachi", 78: "Whistle", 79: "Ocarina",
    # Synth Lead
    80: "Lead 1 (square)", 81: "Lead 2 (sawtooth)", 82: "Lead 3 (calliope)", 83: "Lead 4 (chiff)",
    84: "Lead 5 (charang)", 85: "Lead 6 (voice)", 86: "Lead 7 (fifths)", 87: "Lead 8 (bass + lead)",
    # Synth Pad
    88: "Pad 1 (new age)", 89: "Pad 2 (warm)", 90: "Pad 3 (polysynth)", 91: "Pad 4 (choir)",
    92: "Pad 5 (bowed)", 93: "Pad 6 (metallic)", 94: "Pad 7 (halo)", 95: "Pad 8 (sweep)",
    # Synth Effects
    96: "FX 1 (rain)", 97: "FX 2 (soundtrack)", 98: "FX 3 (crystal)", 99: "FX 4 (atmosphere)",
    100: "FX 5 (brightness)", 101: "FX 6 (goblins)", 102: "FX 7 (echoes)", 103: "FX 8 (sci-fi)",
    # Ethnic
    104: "Sitar", 105: "Banjo", 106: "Shamisen", 107: "Koto",
    108: "Kalimba", 109: "Bagpipe", 110: "Fiddle", 111: "Shanai",
    # Percussive
    112: "Tinkle Bell", 113: "Agogo", 114: "Steel Drums", 115: "Woodblock",
    116: "Taiko Drum", 117: "Melodic Tom", 118: "Synth Drum", 119: "Reverse Cymbal",
    # Sound Effects
    120: "Guitar Fret Noise", 121: "Breath Noise", 122: "Seashore", 123: "Bird Tweet",
    124: "Telephone Ring", 125: "Helicopter", 126: "Applause", 127: "Gunshot"
}

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GoogleBand Mega Studio</title>
    <style>
        body { background: #121212; color: #fff; text-align: center; font-family: sans-serif; margin: 0; padding: 10px; }
        h1 { color: #00ffcc; font-size: 18px; margin: 5px 0; }
        .panel { background: #1e1e1e; padding: 10px; border-radius: 8px; margin-top: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.4); }
        .label { font-size: 13px; color: #ff007f; margin-bottom: 6px; font-weight: bold; }
        select { background: #333; color: #fff; padding: 8px; font-size: 13px; border-radius: 4px; border: 1px solid #555; width: 100%; max-width: 320px; }
        .container { display: flex; justify-content: center; gap: 3px; flex-wrap: wrap; margin-top: 5px; }
        .key { background: #fff; color: #000; width: 34px; height: 110px; border-radius: 3px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 6px; font-weight: bold; font-size: 11px; cursor: pointer; user-select: none; }
        .key:active { background: #00ffcc; }
        .string-btn { background: #ff5722; color: white; width: 55px; height: 38px; border-radius: 19px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 12px; cursor: pointer; user-select: none; }
        .string-btn:active { background: #ffeb3b; color: #000; }
        .rhythm-btn { background: #9c27b0; color: white; padding: 8px 12px; border-radius: 5px; border: none; font-weight: bold; cursor: pointer; font-size: 12px; margin: 3px; }
        .rhythm-btn:active { background: #e040fb; }
    </style>
</head>
<body>
    <h1>GoogleBand Mega Studio</h1>
    <p style="font-size: 11px; color: #888; margin: 0 0 10px 0;">All 128 General MIDI Instruments Unlocked</p>

    <div class="panel">
        <div class="label">🎛️ Select Instrument (128 Choices)</div>
        <select id="instrument" onchange="updateInstrument()">
            {% for prog, name in instruments.items() %}
            <option value="{{ prog }}">{{ prog }}: {{ name }}</option>
            {% endfor %}
        </select>
    </div>

    <div class="panel">
        <div class="label">🎹 Full Keyboard (Octaves 3 & 4)</div>
        <div class="container">
            <div class="key" onclick="playNote('C3')">C3</div>
            <div class="key" onclick="playNote('D3')">D3</div>
            <div class="key" onclick="playNote('E3')">E3</div>
            <div class="key" onclick="playNote('F3')">F3</div>
            <div class="key" onclick="playNote('G3')">G3</div>
            <div class="key" onclick="playNote('A3')">A3</div>
            <div class="key" onclick="playNote('B3')">B3</div>
            <div class="key" onclick="playNote('C4')">C4</div>
            <div class="key" onclick="playNote('D4')">D4</div>
            <div class="key" onclick="playNote('E4')">E4</div>
            <div class="key" onclick="playNote('F4')">F4</div>
            <div class="key" onclick="playNote('G4')">G4</div>
            <div class="key" onclick="playNote('A4')">A4</div>
            <div class="key" onclick="playNote('B4')">B4</div>
            <div class="key" onclick="playNote('C5')">C5</div>
        </div>
    </div>

    <div class="panel">
        <div class="label">🎸 Quick Strings / Plucks</div>
        <div class="container">
            <div class="string-btn" onclick="playNote('E2')">E2</div>
            <div class="string-btn" onclick="playNote('A2')">A2</div>
            <div class="string-btn" onclick="playNote('D3')">D3</div>
            <div class="string-btn" onclick="playNote('G3')">G3</div>
            <div class="string-btn" onclick="playNote('B3')">B3</div>
        </div>
    </div>

    <div class="panel">
        <div class="label">🥁 Rhythm Beats</div>
        <div>
            <button class="rhythm-btn" onclick="playRhythm('rock')">Rock</button>
            <button class="rhythm-btn" onclick="playRhythm('hiphop')">Hip-Hop</button>
            <button class="rhythm-btn" onclick="playRhythm('jazz')">Jazz</button>
        </div>
    </div>

    <script>
        let currentInst = '0';
        function updateInstrument() { currentInst = document.getElementById('instrument').value; }
        
        function playNote(note) {
            let audio = new Audio('/play?note=' + note + '&inst=' + currentInst);
            audio.play().catch(e => console.log(e));
        }
        
        function playRhythm(style) {
            let audio = new Audio('/rhythm?style=' + style);
            audio.play().catch(e => console.log(e));
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE, instruments=GM_INSTRUMENTS)

@app.route('/play')
def play():
    note_name = request.args.get('note', 'C4')
    prog_num = int(request.args.get('inst', '0'))
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    track.append(mido.Message('program_change', program=prog_num, time=0))
    track.append(mido.Message('note_on', note=NOTE_MAP.get(note_name, 60), velocity=90, time=0))
    track.append(mido.Message('note_off', note=NOTE_MAP.get(note_name, 60), velocity=90, time=480))
    mid.save('live.mid')
    os.system('fluidsynth -ni -F out.wav general.sf2 live.mid >/dev/null 2>&1')
    return send_file('out.wav', mimetype='audio/wav')

@app.route('/rhythm')
def rhythm():
    style = request.args.get('style', 'rock')
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    beats = {
        'rock': [(36, 0), (42, 0), (38, 240), (42, 240), (36, 480), (42, 480), (38, 720), (42, 720)],
        'hiphop': [(36, 0), (42, 120), (42, 240), (38, 360), (36, 480), (42, 600), (38, 720)],
        'jazz': [(51, 0), (42, 160), (42, 320), (51, 480), (42, 640)]
    }
    last_t = 0
    for note, t in beats.get(style, beats['rock']):
        track.append(mido.Message('note_on', channel=9, note=note, velocity=90, time=max(0, t - last_t)))
        track.append(mido.Message('note_off', channel=9, note=note, velocity=90, time=120))
        last_t = t + 120
    mid.save('rhythm.mid')
    os.system('fluidsynth -ni -F out_rhythm.wav general.sf2 rhythm.mid >/dev/null 2>&1')
    return send_file('out_rhythm.wav', mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
