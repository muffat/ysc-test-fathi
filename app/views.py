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
    activity = songs_backend().songs_page(current_page, limit_item)

    template = render_template("songs_index.html", **locals())
    minified_template = html_minify(template)
    return minified_template

@app.route("/songs/avg/difficulty/", methods=['GET'])
def songs_avg_difficulty():
    level = request.args.get('level')
    if level == None:
        return "Please specify the level, i.e : /songs/avg/difficulty?level=10"
    activity = songs_backend().songs_level(level)
    songs_avg = songs_backend().avg_difficulty(activity)

    template = render_template("songs_level.html", **locals())
    minified_template = html_minify(template)
    return minified_template

@app.route("/songs/search/", methods=['GET'])
def songs_search():
    query = request.args.get('message')
    activity = songs_backend().songs_search(query)

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