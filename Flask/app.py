from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def say_hello():
    return  render_template('home.html')


