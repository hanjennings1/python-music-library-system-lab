# Song Class (represents a single song and tracks stats across all songs)
class Song:

    # Class Attributes:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__ (self, name, artist, genre):
        # Instance attributes — unique to this song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level stats every time a new song is created:
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # Add Song to Count - class method
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Add to Genres - class method
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    #Add to Artists - class method
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    #Add to Genre Count - class method
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    #Add to Artist Count - class method
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1