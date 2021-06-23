from flask_app import app
from flask import  render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# app = Flask(__name__) 


@app.route('/')
def index():
    return redirect('/dojos')

# -------------------first page/ create-------------


@app.route('/dojos')
def getall():
    dojos = Dojo.get_all()
    print (dojos)
    return render_template("dojo.html", dojos = dojos)

@app.route('/dojo/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name' : request.form['name']
    }
    Dojo.save(data)
    return redirect ('/dojos')


# ----------------------------show ninjas in dojo--------------------------------



@app.route('/showdojo/<int:id>')
def showdojosninjas(id):
    data = {
        'id': id 
    }
    dojos = Dojo.get_dojo_with_ninjas(data)

    return render_template('showdojo.html', dojo = dojos)


