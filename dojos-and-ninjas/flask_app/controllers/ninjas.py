from flask_app import app
from flask import  render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/showdojo/<int:id>')
def getallninjas(id):
    data = {
        "id": id
    }
    print(data)
    ninjas = Ninja.get_by_dojoid()
    print (ninjas)
    return render_template("showdojo.html", ninjas = ninjas)


@app.route('/dojo/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    
    Ninja.save(data)
    return redirect ('/dojo')



@app.route("/makeninja")
def makeninja():
    dojos = Dojo.get_all()
    print (dojos)
    return render_template("createninja.html", dojos = dojos)

