import ipdb
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    def add_song_to_count(cls, increment = 1):
        Song.count += increment

    def add_to_genres(self):
        Song.genres.append(self.genre)
    def add_to_artists(self):
        Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
         Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1


    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
        pass

    # genre = "pop", "rock", "chuuuuu", "pop", "rock", "rock"
    # genres = []
    # genres.append(genre)
    # print(genres)
    # genre_count = {}
    # for g in genre:
    #     if g in genre_count:
    #      genre_count[g] += 1
    #     else:
    #      genre_count[g] = 1

    # unique_list = list(set(genre))
    # print(unique_list)
    # print(genre_count)
