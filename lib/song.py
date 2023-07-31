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
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
         cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
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
