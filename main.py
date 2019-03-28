import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    tom_movie = get_random_movie()

    tom_content = "<h1>Tomorrow's Movie</h1>"
    tom_content += "<ul>"
    tom_content += "<li>" + tom_movie + "</li>"
    tom_content += "</ul>"

    return content + tom_content

def get_random_movie():
    
    # TODO: make a list with at least 5 movie titles
    movie_list = ["movie1", "movie2", "movie3", "movie4", "movie5"]
    # TODO: randomly choose one of the movies, and return it
    selected_movie = random.choice(movie_list)
    #return "The Big Lebowski"
    return selected_movie

    #tom_selected_movie = random.choice(movie_list)
    #return tom_selected_movie
    #if tom_selected_movie != selected_movie:
    #    return tom_selected_movie
    #else:
    #    return tom_selected_movie + 1


app.run()
