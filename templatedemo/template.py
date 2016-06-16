from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def index():
    return render_template('main.html',
            title="Learning about Flask!",
            greet="Hello World!") 

@app.route("/hello/<name>")
def hello(name):
    return render_template('main.html',
            title="Learning about Flask!",
            greet="Hello {}".format(name.capitalize()))

if __name__ == "__main__":
    app.run()
