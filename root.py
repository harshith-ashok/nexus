from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('root.html')


if __name__ == '__main__':
    app.run(debug=True)
