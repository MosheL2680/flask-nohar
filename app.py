from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/nohar")
def nohar():
    return render_template('nohar.html')



if __name__ == '__main__':
    app.run(debug=True)