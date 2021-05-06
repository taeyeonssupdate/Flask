from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "傻逼酷誒單", 200


@app.route('/indexx')
def indexx():
    return render_template('index.html'), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
