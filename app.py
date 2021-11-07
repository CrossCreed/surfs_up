from flask import Flask




# ----- Set up Flask -----
app = Flask(__name__)
# "Instance" - general term in programming to refer to signular version of something
# __name__ variable denotes the name of the function
# variables with underscores before and after are called magic methods in Python

# Define starting point or "root"
# THe forward slash denotes we want to put our data at the root of our route
@app.route('/')
def hello_world():
    return 'Hello world'
    
