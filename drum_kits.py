"""GoogleBand Drum Kits - Extended drum sounds and kits"""

class DrumKits:
    DRUM_SOUNDS = {
        'kick': 36, 'snare': 38, 'hihat_closed': 42, 'hihat_open': 46,
        'tom_high': 50, 'tom_mid': 48, 'tom_low': 45, 'cowbell': 56,
        'clap': 39, 'crash': 49, 'ride': 51, 'china': 52,
    }
    
    DRUM_KITS = {
        'rock': {'kick': 36, 'snare': 38, 'hihat': 42, 'tom_high': 50, 'tom_mid': 48, 'tom_low': 45, 'crash': 49},
        'hiphop': {'kick': 36, 'snare': 40, 'hihat_closed': 42, 'hihat_open': 46, 'clap': 39, 'cowbell': 56},
        'jazz': {'kick': 36, 'snare': 38, 'hihat': 42, 'ride': 51},
        'pop': {'kick': 36, 'snare': 38, 'hihat': 42, 'tom_mid': 48, 'clap': 39},
        'latin': {'kick': 36, 'conga': 63, 'cowbell': 56},
        'electronic': {'kick': 36, 'snare': 40, 'hihat_closed': 42, 'hihat_open': 46},
    }
    
    DRUM_PATTERNS = {
        'rock_4x4': {'kick': [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0], 'snare': [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]},
        'hiphop_trap': {'kick': [1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0], 'snare': [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]},
        'jazz_swing': {'kick': [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]},
        'pop_upbeat': {'kick': [1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0]},
        'latin_salsa': {'kick': [1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1]},
        'electronic_industrial': {'kick': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]},
    }
    
    @classmethod
    def get_drum_kit(cls, kit_name):
        return cls.DRUM_KITS.get(kit_name, cls.DRUM_KITS['rock'])
    
    @classmethod
    def get_pattern(cls, pattern_name):
        return cls.DRUM_PATTERNS.get(pattern_name)
