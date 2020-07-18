from main import app 

@app.route('/')
def home():
    return("You've set up Flask API Template")