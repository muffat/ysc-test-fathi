import json

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
    def give_songs_rating(song_id, rating):
        rating = int(rating)
        song_id = int(song_id)
        if rating > 0 and rating < 6:
            jsonFile = open("/app/data.json", "r")
            data = json.load(jsonFile)
            songs = []
            for song in data:
                if song['song_id'] == song_id:
                    ratings = song['rating']
                    ratings.append(rating)
                songs.append(song)
            jsonFile = open("/app/data.json", "w+")
            jsonFile.write(json.dumps(songs))
            jsonFile.close()
            return True
        else:
            return False

    @staticmethod
    def songs_finder(song_id, param):
        song_id = int(song_id)
        songs = []
        jsonFile = open("/app/data.json", "r")
        data = json.load(jsonFile)
        rating = []
        for song in data:
            if song['song_id'] == song_id:
                rating.append(song['rating'])
        if param == "average":
            if len(rating[0]) == 0:
                result = 0
            else:
                result = sum(rating[0]) / len(rating[0])
        if param == "highest":
            if len(rating[0]) == 0:
                result = 0
            else:
                result = max(rating[0])
        if param == "lowest":
            if len(rating[0]) == 0:
                result = 0
            else:
                result = min(rating[0])
        return result

    @staticmethod
    def song_details(song_id):
        song_id = int(song_id)
        jsonFile = open("/app/data.json", "r")
        data = json.load(jsonFile)
        songs = []
        for song in data:
            if song['song_id'] == song_id:
                songs.append(song)
        return songs

    @staticmethod
    def avg_difficulty(songs):
        avg = []
        for song in songs:
            avg.append(song['difficulty'])
        total_songs = len(avg)
        sum_songs = sum(avg)
        avg = sum_songs/total_songs
        return avg