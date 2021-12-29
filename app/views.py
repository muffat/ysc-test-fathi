from app import app
from app.backends import *
from htmlmin.minify import html_minify
from flask import render_template, request, jsonify

@app.route("/health/", methods=['GET'])
def healthcheck():
    return "HEALTHY"

@app.route("/songs/", methods=['GET'])
@app.route("/songs/<int:pagenumber>/", methods=['GET'])
def songs_index(pagenumber=None):
    limit_item = 3
    if pagenumber is None:
        current_page = 1
    else:
        current_page = pagenumber
    full_url = request.path
    full_urls = full_url.split("/")
    ds = [{"artist":"The Yousicians","title":"Lycanthropic Metamorphosis","difficulty":14.6,"level":13,"released":"2016-10-26"},{"artist":"The Yousicians","title":"A New Kennel","difficulty":9.1,"level":9,"released":"2010-02-03"},{"artist":"Mr Fastfinger","title":"Awaki-Waki","difficulty":15,"level":13,"released":"2012-05-11"},{"artist":"The Yousicians","title":"You've Got The Power","difficulty":13.22,"level":13,"released":"2014-12-20"},{"artist":"The Yousicians","title":"Wishing In The Night","difficulty":10.98,"level":9,"released":"2016-01-01"},{"artist":"The Yousicians","title":"Opa Opa Ta Bouzoukia","difficulty":14.66,"level":13,"released":"2013-04-27"},{"artist":"The Yousicians","title":"Greasy Fingers - boss level","difficulty":2,"level":3,"released":"2016-03-01"},{"artist":"The Yousicians","title":"Alabama Sunrise","difficulty":5,"level":6,"released":"2016-04-01"},{"artist":"The Yousicians","title":"Can't Buy Me Skills","difficulty":9,"level":9,"released":"2016-05-01"},{"artist":"The Yousicians","title":"Vivaldi Allegro Mashup","difficulty":13,"level":13,"released":"2016-06-01"},{"artist":"The Yousicians","title":"Babysitting","difficulty":7,"level":6,"released":"2016-07-01"}]
    activity = songs_backend().songs_page(current_page, limit_item, ds)

    template = render_template("songs_index.html", **locals())
    minified_template = html_minify(template)
    return minified_template

@app.route("/songs/avg/difficulty/", methods=['GET'])
def songs_avg_difficulty():
    ds = [{"artist":"The Yousicians","title":"Lycanthropic Metamorphosis","difficulty":14.6,"level":13,"released":"2016-10-26"},{"artist":"The Yousicians","title":"A New Kennel","difficulty":9.1,"level":9,"released":"2010-02-03"},{"artist":"Mr Fastfinger","title":"Awaki-Waki","difficulty":15,"level":13,"released":"2012-05-11"},{"artist":"The Yousicians","title":"You've Got The Power","difficulty":13.22,"level":13,"released":"2014-12-20"},{"artist":"The Yousicians","title":"Wishing In The Night","difficulty":10.98,"level":9,"released":"2016-01-01"},{"artist":"The Yousicians","title":"Opa Opa Ta Bouzoukia","difficulty":14.66,"level":13,"released":"2013-04-27"},{"artist":"The Yousicians","title":"Greasy Fingers - boss level","difficulty":2,"level":3,"released":"2016-03-01"},{"artist":"The Yousicians","title":"Alabama Sunrise","difficulty":5,"level":6,"released":"2016-04-01"},{"artist":"The Yousicians","title":"Can't Buy Me Skills","difficulty":9,"level":9,"released":"2016-05-01"},{"artist":"The Yousicians","title":"Vivaldi Allegro Mashup","difficulty":13,"level":13,"released":"2016-06-01"},{"artist":"The Yousicians","title":"Babysitting","difficulty":7,"level":6,"released":"2016-07-01"}]

    level = request.args.get('level')
    activity = songs_backend().songs_level(level, ds)
    songs_avg = songs_backend().avg_difficulty(activity)

    template = render_template("songs_level.html", **locals())
    minified_template = html_minify(template)
    return minified_template

@app.route("/songs/search/", methods=['GET'])
def songs_search():
    ds = [{"artist":"The Yousicians","title":"Lycanthropic Metamorphosis","difficulty":14.6,"level":13,"released":"2016-10-26"},{"artist":"The Yousicians","title":"A New Kennel","difficulty":9.1,"level":9,"released":"2010-02-03"},{"artist":"Mr Fastfinger","title":"Awaki-Waki","difficulty":15,"level":13,"released":"2012-05-11"},{"artist":"The Yousicians","title":"You've Got The Power","difficulty":13.22,"level":13,"released":"2014-12-20"},{"artist":"The Yousicians","title":"Wishing In The Night","difficulty":10.98,"level":9,"released":"2016-01-01"},{"artist":"The Yousicians","title":"Opa Opa Ta Bouzoukia","difficulty":14.66,"level":13,"released":"2013-04-27"},{"artist":"The Yousicians","title":"Greasy Fingers - boss level","difficulty":2,"level":3,"released":"2016-03-01"},{"artist":"The Yousicians","title":"Alabama Sunrise","difficulty":5,"level":6,"released":"2016-04-01"},{"artist":"The Yousicians","title":"Can't Buy Me Skills","difficulty":9,"level":9,"released":"2016-05-01"},{"artist":"The Yousicians","title":"Vivaldi Allegro Mashup","difficulty":13,"level":13,"released":"2016-06-01"},{"artist":"The Yousicians","title":"Babysitting","difficulty":7,"level":6,"released":"2016-07-01"}]

    query = request.args.get('message')
    activity = songs_backend().songs_search(query, ds)

    template = render_template("songs_search.html", **locals())
    minified_template = html_minify(template)
    return minified_template

@app.route("/songs/rating/", methods=['POST'])
@app.route("/songs/rating/<int:song_id>/", methods=['GET'])
def songs_rating(song_id=None):
    response_data = {}
    if request.method == "POST":
        song_id = request.form['song_id']
        rating = request.form['rating']
        test = songs_backend().give_songs_rating(song_id, rating)
        if test == True:
            response_data['message'] = "success"
            return jsonify(response_data)
        else:
            response_data['message'] = "error"
            return jsonify(response_data), 400
    else:
        activity = songs_backend().song_details(song_id)
        average_rating = songs_backend().songs_finder(song_id, "average")
        highest_rating = songs_backend().songs_finder(song_id, "highest")
        lowest_rating = songs_backend().songs_finder(song_id, "lowest")
        template = render_template("songs_rating.html", **locals())
        minified_template = html_minify(template)
        return minified_template