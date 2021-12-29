import json

json_str = [{"artist":"The Yousicians","title":"Lycanthropic Metamorphosis","difficulty":14.6,"level":13,"released":"2016-10-26"},{"artist":"The Yousicians","title":"A New Kennel","difficulty":9.1,"level":9,"released":"2010-02-03"},{"artist":"Mr Fastfinger","title":"Awaki-Waki","difficulty":15,"level":13,"released":"2012-05-11"},{"artist":"The Yousicians","title":"You've Got The Power","difficulty":13.22,"level":13,"released":"2014-12-20"},{"artist":"The Yousicians","title":"Wishing In The Night","difficulty":10.98,"level":9,"released":"2016-01-01"},{"artist":"The Yousicians","title":"Opa Opa Ta Bouzoukia","difficulty":14.66,"level":13,"released":"2013-04-27"},{"artist":"The Yousicians","title":"Greasy Fingers - boss level","difficulty":2,"level":3,"released":"2016-03-01"},{"artist":"The Yousicians","title":"Alabama Sunrise","difficulty":5,"level":6,"released":"2016-04-01"},{"artist":"The Yousicians","title":"Can't Buy Me Skills","difficulty":9,"level":9,"released":"2016-05-01"},{"artist":"The Yousicians","title":"Vivaldi Allegro Mashup","difficulty":13,"level":13,"released":"2016-06-01"},{"artist":"The Yousicians","title":"Babysitting","difficulty":7,"level":6,"released":"2016-07-01"}]

songs = []

for i in json_str:
    if i['level'] == 13:
        songs.append(i)

print(songs)