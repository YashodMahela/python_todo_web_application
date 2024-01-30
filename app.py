#This line imports the Flask class from the flask module.
from flask import Flask
#This line creates a new instance of the Flask class and assigns it to the variable app.
# The __name__ argument is a special Python variable that represents the name of the current module.
# In this case, it’s used to tell Flask where to find the application’s resources.
app = Flask(__name__)

#This code defines a new route for the web application.
# The @app.route('/') decorator tells Flask that this function should be called when the user visits the root URL of the application.
# The index() function returns the string “Hello World” as the response to the user’s request.
@app.route('/')
def index():
    return "Hello World"

#This code starts the Flask development server if the script is run directly (as opposed to being imported as a module).
# The debug=True argument enables debug mode, which provides more detailed error messages and automatically reloads the server when changes are made to the code.
if __name__ == "__main__":
    app.run(debug=True)