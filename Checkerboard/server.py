from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html", num = 4, rowl = 4)


@app.route("/<int:numTimes>")
def repeat(numTimes):
    return render_template("index.html", num = numTimes, rowl = 4)

@app.route("/<int:numTimes>/<int:rowAmount>")
def howmanyrows(numTimes, rowAmount):
    return render_template("index.html", num = numTimes, rowl = rowAmount//2)



if __name__ == "__main__":
    app.run(debug=True)