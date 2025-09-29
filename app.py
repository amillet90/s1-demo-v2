from flask import Flask, request, render_template, redirect, flash
import datetime

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
app.config["TEMPLATES_AUTO_RELOAD"] = True

liste_etudiants = [
    {'id':1,'nom':'tom', 'groupe':'A1'},
    {'id':2,'nom':'enzo', 'groupe':'A1'},
    {'id':3,'nom':'laurence', 'groupe':'A2'},
    {'id':4,'nom':'theo', 'groupe':'A2'},
    {'id':5,'nom':'mehdi', 'groupe':'B1'}
]

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

@app.route('/etudiant/show')
def show_etudiants():
    return render_template('etudiant/show_etudiant.html', etudiants=liste_etudiants )

@app.route('/etudiant/add')
def add_etudiant():
    print('''affichage du formulaire pour saisir un étudiant''')
    return render_template('etudiant/add_etudiant.html')

@app.route('/etudiant/delete')
def delete_etudiant():
    print('''suppression d'un étudiant''')

@app.route('/etudiant/edit')
def edit_etudiant():
    print('''affichage du formulaire pour modifier un étudiant''')
    return render_template('etudiant/edit_etudiant.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
