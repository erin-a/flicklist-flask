from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

header = """
    <!DOCTYPE html>
            <html>
                <head>
                    <title>Flicklist</title>
                </head>
                <body>
                    <h1>Welcome to Flicklist</h1>
    """

footer="""
            </body>
        </html>
    """

@app.route("/add")
def add_movie():
    new_movie = request.args.get("movie")
    
    content = header + "<p>" + new_movie + " has been added to your watchlist.</p>" + footer

    return content

@app.route("/")
# create form that allows user to tell us what movies they want to watch
# add it to list

def index():
    content = header + """
                <form action="/add" method="get">
                    <label for="movie">I want to add
                    <input type="text" name="movie" id="movie" />
                    to my watchlist.</label>
                    <input type="submit" value="Add it" />
                </form?
    """ + footer

    return content

app.run()
