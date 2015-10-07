from random import choice

from flask import Flask, request, render_template


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
   <a href="/hello">"Hi! This is the home crazy page."</a>
        </body>
    </html>

    """


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form["person"]

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
