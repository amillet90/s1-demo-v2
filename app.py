from flask import Flask, request, render_template, redirect, flash


app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!<a href="hello">lien hello</a>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
