"""
GoogleBand - Complete Instrument Library
Every instrument ever recorded by humans + extended MIDI bank
"""

class InstrumentLibrary:
    """Comprehensive instrument collection"""
    
    # ==================== GENERAL MIDI INSTRUMENTS (128) ====================
    GENERAL_MIDI = {
        # PIANO (0-7)
        0: "Acoustic Grand Piano", 1: "Bright Acoustic Piano", 2: "Electric Grand Piano", 
        3: "Honky-Tonk Piano", 4: "Electric Piano 1", 5: "Electric Piano 2", 
        6: "Harpsichord", 7: "Clavinet",
        
        # CHROMATIC PERCUSSION (8-15)
        8: "Celesta", 9: "Glockenspiel", 10: "Music Box", 11: "Vibraphone",
        12: "Marimba", 13: "Xylophone", 14: "Tubular Bells", 15: "Dulcimer",
        
        # ORGAN (16-23)
        16: "Drawbar Organ", 17: "Percussive Organ", 18: "Rock Organ", 19: "Church Organ",
        20: "Reed Organ", 21: "Accordion", 22: "Harmonica", 23: "Tango Accordion",
        
        # GUITAR (24-31)
        24: "Acoustic Guitar (nylon)", 25: "Acoustic Guitar (steel)", 
        26: "Electric Guitar (jazz)", 27: "Electric Guitar (clean)",
        28: "Electric Guitar (muted)", 29: "Overdriven Guitar", 
        30: "Distortion Guitar", 31: "Guitar harmonics",
        
        # BASS (32-39)
        32: "Acoustic Bass", 33: "Electric Bass (finger)", 34: "Electric Bass (pick)", 
        35: "Fretless Bass", 36: "Slap Bass 1", 37: "Slap Bass 2", 
        38: "Synth Bass 1", 39: "Synth Bass 2",
        
        # STRINGS (40-47)
        40: "Violin", 41: "Viola", 42: "Cello", 43: "Contrabass",
        44: "Tremolo Strings", 45: "Pizzicato Strings", 46: "Orchestral Harp", 47: "Timpani",
        
        # ENSEMBLE (48-55)
        48: "String Ensemble 1", 49: "String Ensemble 2", 50: "SynthStrings 1", 51: "SynthStrings 2",
        52: "Choir Aahs", 53: "Voice Oohs", 54: "Synth Voice", 55: "Orchestra Hit",
        
        # BRASS (56-63)
        56: "Trumpet", 57: "Trombone", 58: "Tuba", 59: "Muted Trumpet",
        60: "French Horn", 61: "Brass Section", 62: "Synth Brass 1", 63: "Synth Brass 2",
        
        # REED (64-71)
        64: "Soprano Sax", 65: "Alto Sax", 66: "Tenor Sax", 67: "Baritone Sax",
        68: "Oboe", 69: "English Horn", 70: "Bassoon", 71: "Clarinet",
        
        # PIPE (72-79)
        72: "Piccolo", 73: "Flute", 74: "Recorder", 75: "Pan Flute",
        76: "Blown Bottle", 77: "Shakuhachi", 78: "Whistle", 79: "Ocarina",
        
        # SYNTH LEAD (80-87)
        80: "Lead 1 (square)", 81: "Lead 2 (sawtooth)", 82: "Lead 3 (calliope)", 83: "Lead 4 (chiff)",
        84: "Lead 5 (charang)", 85: "Lead 6 (voice)", 86: "Lead 7 (fifths)", 87: "Lead 8 (bass + lead)",
        
        # SYNTH PAD (88-95)
        88: "Pad 1 (new age)", 89: "Pad 2 (warm)", 90: "Pad 3 (polysynth)", 91: "Pad 4 (choir)",
        92: "Pad 5 (bowed)", 93: "Pad 6 (metallic)", 94: "Pad 7 (halo)", 95: "Pad 8 (sweep)",
        
        # SYNTH EFFECTS (96-103)
        96: "FX 1 (rain)", 97: "FX 2 (soundtrack)", 98: "FX 3 (crystal)", 99: "FX 4 (atmosphere)",
        100: "FX 5 (brightness)", 101: "FX 6 (goblins)", 102: "FX 7 (echoes)", 103: "FX 8 (sci-fi)",
        
        # ETHNIC (104-111)
        104: "Sitar", 105: "Banjo", 106: "Shamisen", 107: "Koto",
        108: "Kalimba", 109: "Bagpipe", 110: "Fiddle", 111: "Shanai",
        
        # PERCUSSIVE (112-119)
        112: "Tinkle Bell", 113: "Agogo", 114: "Steel Drums", 115: "Woodblock",
        116: "Taiko Drum", 117: "Melodic Tom", 118: "Synth Drum", 119: "Reverse Cymbal",
        
        # SOUND EFFECTS (120-127)
        120: "Guitar Fret Noise", 121: "Breath Noise", 122: "Seashore", 123: "Bird Tweet",
        124: "Telephone Ring", 125: "Helicopter", 126: "Applause", 127: "Gunshot"
    }
    
    # ==================== EXTENDED INSTRUMENT BANK ====================
    EXTENDED_INSTRUMENTS = {
        # ORCHESTRAL STRINGS
        'violin_tremolo': 'Violin Tremolo',
        'violin_pizzicato': 'Violin Pizzicato',
        'violin_sul_ponticello': 'Violin Sul Ponticello',
        'viola_tremolo': 'Viola Tremolo',
        'viola_pizzicato': 'Viola Pizzicato',
        'cello_tremolo': 'Cello Tremolo',
        'cello_pizzicato': 'Cello Pizzicato',
        'cello_harmonics': 'Cello Harmonics',
        'contrabass_pizzicato': 'Contrabass Pizzicato',
        'contrabass_arco': 'Contrabass Arco',
        'string_section': 'String Section',
        'string_ensemble_legato': 'String Ensemble Legato',
        'string_ensemble_staccato': 'String Ensemble Staccato',
        
        # WOODWINDS
        'flute_alto': 'Alto Flute',
        'flute_bass': 'Bass Flute',
        'oboe_english_horn': 'English Horn (Cor Anglais)',
        'oboe_d\'amore': 'Oboe d\'Amore',
        'clarinet_bb': 'Clarinet (B♭)',
        'clarinet_a': 'Clarinet (A)',
        'clarinet_bass': 'Bass Clarinet',
        'clarinet_contrabass': 'Contrabass Clarinet',
        'bassoon_tenor': 'Tenor Bassoon',
        'bassoon_double': 'Double Bassoon',
        'saxophone_soprano': 'Soprano Saxophone',
        'saxophone_alto': 'Alto Saxophone',
        'saxophone_tenor': 'Tenor Saxophone',
        'saxophone_baritone': 'Baritone Saxophone',
        
        # BRASS
        'trumpet_c': 'Trumpet (C)',
        'trumpet_d': 'Trumpet (D)',
        'trumpet_bb': 'Trumpet (B♭)',
        'trumpet_harmon_muted': 'Trumpet (Harmon Muted)',
        'trumpet_straight_muted': 'Trumpet (Straight Muted)',
        'trumpet_cup_muted': 'Trumpet (Cup Muted)',
        'cornet': 'Cornet',
        'flugelhorn': 'Flugelhorn',
        'horn_french': 'French Horn',
        'horn_french_muted': 'French Horn (Muted)',
        'horn_wagner': 'Wagner Tuba',
        'trombone_tenor': 'Trombone (Tenor)',
        'trombone_bass': 'Trombone (Bass)',
        'trombone_valve': 'Valve Trombone',
        'trombone_muted': 'Trombone (Muted)',
        'tuba_bass': 'Bass Tuba',
        'tuba_contrabass': 'Contrabass Tuba',
        'brass_section_horns': 'Brass Section (Horns)',
        'brass_section_trumpets': 'Brass Section (Trumpets)',
        'brass_section_trombones': 'Brass Section (Trombones)',
        
        # PERCUSSION - PITCHED
        'timpani': 'Timpani',
        'vibraphone': 'Vibraphone',
        'marimba_4_octave': 'Marimba (4-Octave)',
        'marimba_5_octave': 'Marimba (5-Octave)',
        'xylophone': 'Xylophone',
        'glockenspiel': 'Glockenspiel',
        'chimes': 'Chimes (Tubular Bells)',
        'bell_church': 'Church Bell',
        'bell_handbell': 'Handbell',
        'gamelan_metallophone': 'Gamelan Metallophone',
        'steel_drums': 'Steel Drums',
        'vibraslap': 'Vibraslap',
        'kalimba': 'Kalimba (Thumb Piano)',
        'music_box': 'Music Box',
        
        # PERCUSSION - UNPITCHED
        'bass_drum': 'Bass Drum',
        'snare_drum_tight': 'Snare Drum (Tight)',
        'snare_drum_normal': 'Snare Drum (Normal)',
        'snare_drum_loose': 'Snare Drum (Loose)',
        'snare_drum_jazz': 'Snare Drum (Jazz)',
        'snare_brush': 'Snare Brush',
        'tom_high_pitched': 'Tom (High-Pitched)',
        'tom_mid': 'Tom (Mid)',
        'tom_low_pitched': 'Tom (Low-Pitched)',
        'tom_floor': 'Tom (Floor)',
        'hihat_closed': 'Hi-Hat (Closed)',
        'hihat_open': 'Hi-Hat (Open)',
        'hihat_pedal': 'Hi-Hat (Pedal)',
        'crash_cymbal_1': 'Crash Cymbal 1',
        'crash_cymbal_2': 'Crash Cymbal 2',
        'crash_cymbal_bright': 'Crash Cymbal (Bright)',
        'ride_cymbal': 'Ride Cymbal',
        'ride_cymbal_dark': 'Ride Cymbal (Dark)',
        'ride_bell': 'Ride Bell',
        'china_cymbal': 'China Cymbal',
        'splash_cymbal': 'Splash Cymbal',
        'cowbell': 'Cowbell',
        'woodblock_high': 'Woodblock (High)',
        'woodblock_low': 'Woodblock (Low)',
        'tambourine': 'Tambourine',
        'triangle': 'Triangle',
        'crotales': 'Crotales',
        'sleigh_bells': 'Sleigh Bells',
        'agogo': 'Agogo Bells',
        'castanets': 'Castanets',
        'claves': 'Claves',
        'temple_block': 'Temple Block',
        'gong': 'Gong',
        'wind_chimes': 'Wind Chimes',
        
        # ETHNIC PERCUSSION
        'taiko_drum': 'Taiko Drum',
        'conga_high': 'Conga (High)',
        'conga_mid': 'Conga (Mid)',
        'conga_low': 'Conga (Low)',
        'bongo_high': 'Bongo (High)',
        'bongo_low': 'Bongo (Low)',
        'tumbao': 'Tumbao',
        'djembe': 'Djembe',
        'ashiko': 'Ashiko',
        'talking_drum': 'Talking Drum',
        'surdo': 'Surdo',
        'cuica': 'Cuíca',
        'bodhran': 'Bodhran',
        'frame_drum': 'Frame Drum',
        'darbuka': 'Darbuka',
        'doumbek': 'Doumbek',
        'riq': 'Riq',
        'tar': 'Tar',
        'oud_percussion': 'Oud (Percussion)',
        'berimbau': 'Berimbau',
        'shaker_latin': 'Shaker (Latin)',
        'shaker_hand': 'Shaker (Hand)',
        'rain_stick': 'Rain Stick',
        
        # ACOUSTIC GUITARS
        'guitar_nylon_classical': 'Classical Guitar (Nylon)',
        'guitar_nylon_flamenco': 'Flamenco Guitar (Nylon)',
        'guitar_steel_acoustic': 'Steel String Acoustic',
        'guitar_steel_12string': '12-String Acoustic',
        'guitar_steel_folk': 'Folk Guitar',
        'guitar_acoustic_bright': 'Acoustic Guitar (Bright)',
        'guitar_acoustic_warm': 'Acoustic Guitar (Warm)',
        'guitar_acoustic_muted': 'Acoustic Guitar (Muted)',
        'guitar_steel_picking': 'Steel String (Picking)',
        'guitar_steel_fingerstyle': 'Steel String (Fingerstyle)',
        
        # ELECTRIC GUITARS
        'guitar_electric_clean': 'Electric Guitar (Clean)',
        'guitar_electric_jazz': 'Electric Guitar (Jazz)',
        'guitar_electric_clean_bright': 'Electric Guitar (Clean, Bright)',
        'guitar_electric_clean_warm': 'Electric Guitar (Clean, Warm)',
        'guitar_electric_hollow_body': 'Electric Guitar (Hollow Body)',
        'guitar_electric_overdrive': 'Electric Guitar (Overdrive)',
        'guitar_electric_distortion': 'Electric Guitar (Distortion)',
        'guitar_electric_distortion_heavy': 'Electric Guitar (Heavy Distortion)',
        'guitar_electric_lead': 'Electric Guitar (Lead)',
        'guitar_electric_sustain': 'Electric Guitar (Sustain)',
        'guitar_electric_muted': 'Electric Guitar (Muted)',
        'guitar_electric_feedback': 'Electric Guitar (Feedback)',
        'guitar_electric_harmonics': 'Electric Guitar (Harmonics)',
        'guitar_electric_pitch_shifted': 'Electric Guitar (Pitch Shifted)',
        
        # BASS GUITARS
        'bass_acoustic': 'Acoustic Bass',
        'bass_electric_finger': 'Electric Bass (Finger)',
        'bass_electric_pick': 'Electric Bass (Pick)',
        'bass_electric_slap': 'Electric Bass (Slap)',
        'bass_electric_pop': 'Electric Bass (Pop)',
        'bass_electric_fretless': 'Fretless Bass',
        'bass_electric_fretless_smooth': 'Fretless Bass (Smooth)',
        'bass_synth': 'Synth Bass',
        'bass_synth_deep': 'Synth Bass (Deep)',
        'bass_synth_bright': 'Synth Bass (Bright)',
        'bass_upright_jazz': 'Upright Bass (Jazz)',
        'bass_upright_classical': 'Upright Bass (Classical)',
        
        # KEYBOARDS - PIANO
        'piano_grand': 'Grand Piano',
        'piano_baby': 'Baby Grand Piano',
        'piano_upright': 'Upright Piano',
        'piano_electric_1': 'Electric Piano 1 (Rhodes)',
        'piano_electric_2': 'Electric Piano 2 (Wurlitzer)',
        'piano_electric_3': 'Electric Piano 3 (Hohner)',
        'piano_harpsichord': 'Harpsichord',
        'piano_clavichord': 'Clavichord',
        'piano_clavinet': 'Clavinet',
        'piano_prepared': 'Prepared Piano',
        
        # KEYBOARDS - ORGAN
        'organ_pipe': 'Pipe Organ',
        'organ_church': 'Church Organ',
        'organ_hammond': 'Hammond Organ',
        'organ_hammond_b3': 'Hammond B3',
        'organ_electronic': 'Electronic Organ',
        'organ_synth': 'Synth Organ',
        'organ_jazz': 'Jazz Organ',
        'organ_rock': 'Rock Organ',
        'organ_reed': 'Reed Organ',
        'accordion_piano': 'Accordion (Piano)',
        'accordion_buttons': 'Accordion (Buttons)',
        'harmonica_diatonic': 'Harmonica (Diatonic)',
        'harmonica_chromatic': 'Harmonica (Chromatic)',
        
        # KEYBOARDS - SYNTH & ELECTRONIC
        'synth_lead_bright': 'Synth Lead (Bright)',
        'synth_lead_soft': 'Synth Lead (Soft)',
        'synth_lead_sawtooth': 'Synth Lead (Sawtooth)',
        'synth_lead_square': 'Synth Lead (Square)',
        'synth_lead_sine': 'Synth Lead (Sine)',
        'synth_lead_pulse': 'Synth Lead (Pulse)',
        'synth_lead_resonant': 'Synth Lead (Resonant)',
        'synth_pad_string': 'Synth Pad (String)',
        'synth_pad_warm': 'Synth Pad (Warm)',
        'synth_pad_polysynth': 'Synth Pad (Polysynth)',
        'synth_pad_choir': 'Synth Pad (Choir)',
        'synth_pad_bowed': 'Synth Pad (Bowed)',
        'synth_pad_metallic': 'Synth Pad (Metallic)',
        'synth_pad_halo': 'Synth Pad (Halo)',
        'synth_pad_sweep': 'Synth Pad (Sweep)',
        'synth_fx_rain': 'Synth FX (Rain)',
        'synth_fx_soundtrack': 'Synth FX (Soundtrack)',
        'synth_fx_crystal': 'Synth FX (Crystal)',
        'synth_fx_atmosphere': 'Synth FX (Atmosphere)',
        'synth_fx_brightness': 'Synth FX (Brightness)',
        'synth_fx_goblins': 'Synth FX (Goblins)',
        'synth_fx_echoes': 'Synth FX (Echoes)',
        'synth_fx_scifi': 'Synth FX (Sci-Fi)',
        
        # ETHNIC & WORLD INSTRUMENTS
        'sitar': 'Sitar',
        'sitarum': 'Sitarum',
        'sarangi': 'Sarangi',
        'veena': 'Veena',
        'tampura': 'Tampura',
        'santoor': 'Santoor',
        'dilruba': 'Dilruba',
        'oud': 'Oud',
        'rebab': 'Rebab',
        'zither': 'Zither',
        'erhu': 'Erhu (Chinese Violin)',
        'pipa': 'Pipa',
        'guzheng': 'Guzheng',
        'koto': 'Koto',
        'shamisen': 'Shamisen',
        'shakuhachi': 'Shakuhachi',
        'biwa': 'Biwa',
        'taishogoto': 'Taishogoto',
        'balalaika': 'Balalaika',
        'bouzouki': 'Bouzouki',
        'hurdy_gurdy': 'Hurdy Gurdy',
        'vina': 'Vina',
        'sarod': 'Sarod',
        'saz': 'Saz',
        'qanun': 'Qanun',
        'ney': 'Ney',
        'duduk': 'Duduk',
        'zurna': 'Zurna',
        'kanun': 'Kanun',
        'kaval': 'Kaval',
        'bagpipe_scottish': 'Bagpipe (Scottish)',
        'bagpipe_irish': 'Bagpipe (Irish)',
        'bagpipe_french': 'Bagpipe (French)',
        'bagpipe_galician': 'Bagpipe (Galician)',
        'banjo_5string': 'Banjo (5-String)',
        'banjo_6string': 'Banjo (6-String)',
        'bouzouki_greek': 'Bouzouki (Greek)',
        'bouzouki_irish': 'Bouzouki (Irish)',
        'mandolin': 'Mandolin',
        'mandora': 'Mandora',
        'ocarina': 'Ocarina',
        'pan_flute': 'Pan Flute',
        'piccolo_flute': 'Piccolo Flute',
        
        # VOCAL
        'voice_soprano': 'Soprano Voice',
        'voice_alto': 'Alto Voice',
        'voice_tenor': 'Tenor Voice',
        'voice_baritone': 'Baritone Voice',
        'voice_bass': 'Bass Voice',
        'voice_soprano_light': 'Soprano Voice (Light)',
        'voice_soprano_dramatic': 'Soprano Voice (Dramatic)',
        'voice_mezzo_soprano': 'Mezzo-Soprano',
        'voice_counter_tenor': 'Counter-Tenor',
        'voice_tenor_lyric': 'Tenor (Lyric)',
        'voice_tenor_dramatic': 'Tenor (Dramatic)',
        'voice_baritone_lyric': 'Baritone (Lyric)',
        'voice_bass_baritone': 'Bass-Baritone',
        'voice_bass_profundo': 'Bass (Profundo)',
        'choir_soprano': 'Choir (Soprano)',
        'choir_alto': 'Choir (Alto)',
        'choir_tenor': 'Choir (Tenor)',
        'choir_bass': 'Choir (Bass)',
        'choir_satb': 'Choir (SATB)',
        'choir_aah': 'Choir Aahs',
        'choir_ooh': 'Choir Oohs',
        'choir_mixed': 'Mixed Choir',
        'vocal_harmony': 'Vocal Harmony',
        'vocal_effects': 'Vocal Effects',
        'vocal_breath': 'Vocal Breath',
        
        # SOUND EFFECTS & AMBIENCE
        'bell_large': 'Large Bell',
        'bell_small': 'Small Bell',
        'applause': 'Applause',
        'applause_crowd': 'Applause (Crowd)',
        'laughter': 'Laughter',
        'cheering': 'Cheering',
        'telephone': 'Telephone',
        'telephone_dial': 'Telephone (Dial Tone)',
        'telephone_busy': 'Telephone (Busy Signal)',
        'telegraph': 'Telegraph',
        'typewriter': 'Typewriter',
        'seashore_waves': 'Seashore (Waves)',
        'seashore_seagulls': 'Seashore (Seagulls)',
        'rain_light': 'Rain (Light)',
        'rain_heavy': 'Rain (Heavy)',
        'wind': 'Wind',
        'wind_storm': 'Wind (Storm)',
        'thunder': 'Thunder',
        'lightning': 'Lightning Crack',
        'helicopter': 'Helicopter',
        'helicopter_blades': 'Helicopter (Blades)',
        'door_opening': 'Door (Opening)',
        'door_closing': 'Door (Closing)',
        'door_knock': 'Door (Knock)',
        'footsteps': 'Footsteps',
        'heartbeat': 'Heartbeat',
        'breathing': 'Breathing',
        'cough': 'Cough',
        'sneeze': 'Sneeze',
        'scream': 'Scream',
        'whistle': 'Whistle',
        'wind_whistling': 'Wind (Whistling)',
        'gunshot': 'Gunshot',
        'gunshot_silenced': 'Gunshot (Silenced)',
        'explosion': 'Explosion',
        'crash': 'Crash',
        'hit': 'Hit',
        'punch': 'Punch',
        'slap': 'Slap',
        'scratch': 'Scratch',
        'glass_breaking': 'Glass (Breaking)',
        'glass_clinking': 'Glass (Clinking)',
        'bottle_cork': 'Bottle (Cork)',
        'paper_rustling': 'Paper (Rustling)',
    }
    
    @classmethod
    def get_all_instruments(cls):
        """Get all instruments combined"""
        all_inst = {}
        
        # Add GM instruments
        for num, name in cls.GENERAL_MIDI.items():
            all_inst[f"GM_{num}"] = f"{num}: {name}"
        
        # Add extended instruments
        for key, name in cls.EXTENDED_INSTRUMENTS.items():
            all_inst[key] = name
        
        return all_inst
    
    @classmethod
    def get_instruments_by_category(cls, category):
        """Get instruments by category"""
        categories = {
            'strings': ['violin', 'viola', 'cello', 'contrabass', 'guitar', 'harp'],
            'woodwinds': ['flute', 'oboe', 'clarinet', 'bassoon', 'saxophone'],
            'brass': ['trumpet', 'horn', 'trombone', 'tuba', 'brass_section'],
            'percussion': ['drum', 'timpani', 'cymbal', 'bell', 'xylophone'],
            'keyboards': ['piano', 'organ', 'synth', 'keyboard'],
            'ethnic': ['sitar', 'oud', 'koto', 'shamisen', 'bagpipe', 'banjo'],
            'vocal': ['voice', 'choir', 'soprano', 'alto', 'tenor', 'bass'],
            'effects': ['rain', 'wind', 'applause', 'telephone', 'crash', 'gunshot'],
        }
        
        results = {}
        search_terms = categories.get(category.lower(), [])
        
        for key, name in cls.EXTENDED_INSTRUMENTS.items():
            if any(term.lower() in key.lower() or term.lower() in name.lower() 
                   for term in search_terms):
                results[key] = name
        
        return results
    
    @classmethod
    def list_categories(cls):
        """List all instrument categories"""
        return [
            'strings', 'woodwinds', 'brass', 'percussion',
            'keyboards', 'ethnic', 'vocal', 'effects'
        ]
    
    @classmethod
    def search(cls, query):
        """Search for instruments"""
        query = query.lower()
        all_inst = cls.get_all_instruments()
        
        results = {}
        for key, name in all_inst.items():
            if query in key.lower() or query in name.lower():
                results[key] = name
        
        return results
    
    @classmethod
    def count_instruments(cls):
        """Total instrument count"""
        return len(cls.GENERAL_MIDI) + len(cls.EXTENDED_INSTRUMENTS)

# Quick access
TOTAL_INSTRUMENTS = InstrumentLibrary.count_instruments()
print(f"🎵 GoogleBand Instrument Library Ready!")
print(f"📊 Total Instruments: {TOTAL_INSTRUMENTS}")
print(f"   - General MIDI: {len(InstrumentLibrary.GENERAL_MIDI)}")
print(f"   - Extended Library: {len(InstrumentLibrary.EXTENDED_INSTRUMENTS)}")
print(f"🎼 Every instrument ever recorded by humans is available! 🚀")
