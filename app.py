from flask import Flask, request, render_template, redirect, flash
import datetime

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!<a href="hello">lien hello</a>  &nbsp; <a href="/heure"> heure </a>'

@app.route('/heure')
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template('index_demo.html', h=h,min=m,sec=s )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
