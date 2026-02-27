from flask import Flask

app = Flask(__name__)

#creating entry function for our application
@app.route('/')
def index():
    return "Hello World"

if __name__=="__main__" :
    app.run(debug=True)