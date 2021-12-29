class songs_backend:
    def __init__(self):
        pass
        
    @staticmethod
    def songs_page(page, limit, ds):
        page = page - 1
        paginated = [ds[i:i+limit] for i in range(0, len(ds), limit)]
        return paginated[page]

    @staticmethod
    def songs_level(level, ds):
        level = int(level)
        songs = []
        for song in ds:
            this_level = song['level']
            this_level = int(this_level)
            if song['level'] == level:
                songs.append(song)
        return songs

    @staticmethod
    def songs_search(query, ds):
        songs = []
        for song in ds:
            if song['artist'] == query:
                songs.append(song)
            if song['title'] == query:
                songs.append(song)
        return songs

    @staticmethod
    def give_songs_rating(song_id, rating, ds):
        f = open("data.json", "r")
        data = json.load(jsonFile)
        songs = []
        for song in ds:
            if song['song_id'] == song_id:
                ratings = song['rating']
                if rating > 0 and rating < 6:
                    ratings.append(rating)
            songs.append(song)
        jsonFile = open("data.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()
        return True

    @staticmethod
    def avg_difficulty(songs):
        avg = []
        for song in songs:
            avg.append(song['difficulty'])
        total_songs = len(avg)
        sum_songs = sum(avg)
        avg = sum_songs/total_songs
        return avg