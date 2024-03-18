class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name_param, artist_param, genre_param):
        self.name = name_param
        self.artist = artist_param
        self.genre = genre_param
        self.add_song_to_count()
        self.add_to_genres(genre_param)
        self.add_to_artists(artist_param)
        self.add_to_genre_count(genre_param)
        self.add_to_artist_count(artist_param)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre): #genre is the parameter, a placeholder for the genre 
        # being passed in through the constructor through genre_param. scroll up to the constructor to see
        if genre not in cls.genre_count: # this if statement is checking if the genre being passed in
            # is not in genre_count, the empty dictinary created above which is a class attribute, do the following condition
            cls.genre_count[genre] = 1 # this line adds the genre as a key to our empty dictionary and...
            # sets it equal to 1 
        else: #otherwise if the genre is already in the dictionary 
            # add 1 to its value, which is the purpose of the next line.
            cls.genre_count[genre] += 1 

# key note: In order for class methods to receive instances being passed in they have to be run
# through the constructor as an attribute with whatever desired instances ex: self.add_to_genre_count(genre_param)

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
            

my_song = Song("Like_you", "Jay_z", "Rap")
    