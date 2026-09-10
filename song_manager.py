"""GoogleBand File Manager - Handle saving, loading, and exporting songs"""
import json
import os
from datetime import datetime
import mido

class SongManager:
    def __init__(self, songs_dir='songs', recordings_dir='recordings', exports_dir='exports'):
        self.songs_dir = songs_dir
        self.recordings_dir = recordings_dir
        self.exports_dir = exports_dir
        
        for d in [songs_dir, recordings_dir, exports_dir]:
            if not os.path.exists(d):
                os.makedirs(d)
    
    def create_new_song(self, name=None):
        if not name:
            name = f'song_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        
        song = {
            'name': name,
            'created': datetime.now().isoformat(),
            'bpm': 120,
            'patterns': {},
            'recordings': [],
            'metadata': {'artist': 'Unknown', 'genre': 'Electronic'}
        }
        return song, name
    
    def save_song(self, song, filename=None):
        if not filename:
            filename = song['name']
        filepath = os.path.join(self.songs_dir, f'{filename}.json')
        try:
            with open(filepath, 'w') as f:
                json.dump(song, f, indent=2)
            return True, filepath
        except Exception as e:
            return False, str(e)
    
    def load_song(self, filename):
        filepath = os.path.join(self.songs_dir, f'{filename}.json')
        try:
            with open(filepath, 'r') as f:
                song = json.load(f)
            return True, song
        except Exception as e:
            return False, str(e)
    
    def list_songs(self):
        songs = []
        try:
            for file in os.listdir(self.songs_dir):
                if file.endswith('.json'):
                    songs.append(file[:-5])
        except:
            pass
        return sorted(songs)
