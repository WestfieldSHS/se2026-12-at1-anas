from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movies")
def movies():
    return render_template("movies.html")


@app.route("/shows")
def shows():
    return render_template("shows.html")


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/page1")
def page1():
    return render_template("page1.html")


@app.route("/page2")
def page2():
    return render_template("page2.html")


@app.route("/page3")
def page3():
    return render_template("page3.html")


@app.route("/page4")
def page4():
    return render_template("page4.html")


@app.route("/page5")
def page5():
    return render_template("page5.html")


@app.route("/show1")
def show1():
    return render_template("show1.html")


@app.route("/show2")
def show2():
    return render_template("show2.html")


@app.route("/show3")
def show3():
    return render_template("show3.html")


@app.route("/show4")
def show4():
    return render_template("show4.html")


@app.route("/show5")
def show5():
    return render_template("show5.html")


@app.route("/game1")
def game1():
    return render_template("game1.html")


@app.route("/game2")
def game2():
    return render_template("game2.html")


@app.route("/game3")
def game3():
    return render_template("game3.html")


@app.route("/search")
def search():
    query = request.args.get("q", "").lower()

    movies = {
        "little women": "/page1",
        "basketball diaries": "/page2",
        "five feet apart": "/page3",
        "war for the planet of the apes": "/page4",
        "interstellar": "/page5",
    }

    shows = {
        "game of thrones": "/show3",
        "trollhunters": "/show2",
        "avatar the last airbender": "/show4",
        "gossip girl": "/show5",
        "smallville": "/show1",
    }
    games = {
        "ghost of tsushima": "/game1",
        "silent hill 2": "/game2",
        "firewatch": "/game3",
    }

    for title, link in games.items():
        if query in title:
            return redirect(link)

    # Search movies
    for title, link in movies.items():
        if query in title:
            return redirect(link)

    # Search shows
    for title, link in shows.items():
        if query in title:
            return redirect(link)

    return "No results found."


if __name__ == "__main__":
    app.run(debug=True)
