from midi2audio import FluidSynth

fs = FluidSynth('general.sf2')
fs.midi_to_audio('beat.mid', 'beat.wav')
print("Successfully generated beat.wav!")
