from tinytag import TinyTag
import os
import itertools
from itertools import groupby
from pprint import pprint
import sys

sys.argv

def get_names_and_path_of_files_in_music():  
    filename_and_path = []
    tree = os.walk('music')
    for path, files, folders in tree:
        for name_of_file in folders:
            all_path_to_files_in_music = {}
            all_path_to_files_in_music.update({'name_of_file' : name_of_file, 'path_to_file' : path})
            filename_and_path.append(all_path_to_files_in_music)
    return filename_and_path 
    
def get_list_of_files_in_music():  
    all_path_to_files_in_music = []
    tree = os.walk('music')
    for path, files, folders in tree:
        for files_in_folders in folders:
            all_path_to_files_in_music.append(os.path.join(path, files_in_folders))
    return all_path_to_files_in_music
    
    
    
def get_song_info_from_mp3_tags(all_files_in_music): 
    list_of_tags = []
    for get_tags in all_files_in_music: 
        info_from_tags = TinyTag.get(get_tags)
        tags = {
            'album': info_from_tags.album,        
            'artist': info_from_tags.artist,        
            'duration': info_from_tags.duration,      
            'number_of_track': info_from_tags.track,
            } 

        list_of_tags.append(tags)
    return list_of_tags
    
def join_dicts(song_info, all_path_and_names_to_files_in_music):
    list_with_all_info_about_songs = [{**tags, **name_and_path} for tags,name_and_path in zip(song_info, all_path_and_names_to_files_in_music)]
    return list_with_all_info_about_songs        

def group_songs_by_album_and_printing(join_dicts):
    album = lambda name_of_album: name_of_album['album']
    group_by_album = groupby(join_dicts, album)
    for album_key, name_of_album in group_by_album:
        print("\n", album_key)
        for tags in name_of_album:
            pprint(tags)
            

if __name__ == '__main__': 
    all_path_and_names_to_files_in_music = get_names_and_path_of_files_in_music()
    all_files_in_music = get_list_of_files_in_music()
    song_info = get_song_info_from_mp3_tags(all_files_in_music)
    join_dicts = join_dicts(song_info, all_path_and_names_to_files_in_music)
    grouped_songs = group_songs_by_album_and_printing(join_dicts)