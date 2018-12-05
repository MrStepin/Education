from tinytag import TinyTag
import os
import itertools
from itertools import groupby
from pprint import pprint
import sys
sys.argv
    
def get_list_of_files_in_music():  
    all_path_to_files_in_music = []
    tree = os.walk('music')
    for path, files, folders in tree:
        for files_in_folders in folders:
            all_path_to_files_in_music.append(os.path.join(path, files_in_folders))
    return all_path_to_files_in_music
    
def get_filename_and_path(all_files_in_music):    
    filename_and_path = [list(os.path.split(path)) for path in all_files_in_music]
    return filename_and_path
    
def get_mp3_tags(all_files_in_music):
    list_of_tags = [TinyTag.get(get_tags) for get_tags in all_files_in_music]
    return list_of_tags

def get_list_with_all_info(get_mp3_tags, get_filename_and_path):
    list_with_all_info = list(zip(get_mp3_tags, get_filename_and_path))
    return list_with_all_info   
    
  #никак не получается прикрутить список(имя, путь) в группировку и вывод  
def group_songs_by_album_and_printing(get_list_with_all_info):
    album = lambda album: album.album
    tags = [track_info[0] for track_info in get_list_with_all_info]
    #name_and_path = [track_info[1] for track_info in get_list_with_all_info]
    group_by_album = groupby(tags, album)
    for album_key, track_info in group_by_album:
        print("\n", album_key)
        for tags in track_info:
            print('{2}. {0} {1} сек.'.format(tags.artist, "%.0f"%tags.duration, tags.track))

if __name__ == '__main__': 
    all_files_in_music = get_list_of_files_in_music()
    get_filename_and_path = get_filename_and_path(all_files_in_music)
    get_mp3_tags = get_mp3_tags(all_files_in_music)
    get_list_with_all_info = get_list_with_all_info(get_mp3_tags, get_filename_and_path)
    group_songs_by_album_and_printing(get_list_with_all_info)