from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/play")
def playButton():
    return render_template("play.html", num = 3, color = 'blue')

@app.route("/play/<int:numTimes>")
def repeat(numTimes):
    return render_template("play.html", num = numTimes, color = 'blue' )

@app.route("/play/<int:numTimes>/<color>")
def changeColor(numTimes, color):
    return render_template("play.html", num = numTimes, color = color)




if __name__ == "__main__":
    app.run(debug=True)