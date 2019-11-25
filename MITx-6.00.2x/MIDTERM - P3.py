'''
You are creating a song playlist for your next party. You have a collection of songs that can be represented as a list of tuples. Each tuple has the following elements:

name: the first element, representing the song name (non-empty string)
song_length: the second, element representing the song duration (float >= 0)
song_size: the third, element representing the size on disk (float >= 0)
You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs you pick do not take up more than
 a given amount of space on disk (the sizes should be less than or equal to the max_disk_size).

You decide the best way to achieve your goal is to start with the first song in the given song list. If the first song doesn't fit on disk,
 return an empty list. If there is enough space for this song, add it to the playlist.

For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't already been chosen. You do
 this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm, that returns a list of the song names in the order in which they were chosen, with the first
 element in the list being the song chosen first. Assume song names are unique and all the songs have different sizes on disk and different durations.

You may not mutate any of the arguments.

For example,

If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 12.2, the function will return ['Roar','Wannabe','Timber']
If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 11, the function will return ['Roar','Wannabe']
'''

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    if songs[0][2] > max_size or len(songs) == 0:
        return []
    else:
        pass
    disk = [songs[0][0]]
    if len(songs) == 1:
        return disk
    songs_dict = {}
    for i in songs[1:]:
        songs_dict[i[0]] = i[2]

    songs_temp = []
    sn = songs_dict.copy()
    available  = max_size - songs[0][2]
    song_weights = sorted(list(songs_dict.values()))
    for i in song_weights:
        for k,v in sn.items():
            if i == sn[k]:
                songs_temp.append((k,v))
                sn[k] = 'Used'
            else:
                pass
    
    for i in songs_temp:
        if i[1] < available:
            disk.append(i[0])
            available -= i[1]
        else:
            pass
    
    return disk

