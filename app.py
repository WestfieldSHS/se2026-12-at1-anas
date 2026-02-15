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


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()

    movies = {
        "little women": "/page1",
        "basketball diaries": "/page2",
        "five feet apart": "/page3",
        "war for the planet of the apes": "/page4",
        "interstellar": "/page5",
    }

    if query in movies:
        return redirect(movies[query])

    for title, link in movies.items():
        if query in title.lower():
            return redirect(link)

    return "No results found."


if __name__ == "__main__":
    app.run(debug=True)
