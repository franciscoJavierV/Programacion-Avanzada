## @imports
from flask import Flask
from flask import request
from flask import render_template
from flaskext.mysql import MySQL
import json
##Primeras instancias de flask y la db

app = Flask(__name__, template_folder="../Front", static_folder="../Front")

###ruta renderizado de index
@app.route('/index.html')
def index():   
    return render_template("index.html")
 ### ruta renderizado de pedir   
@app.route('/pedir.html')
def pedir():
    return render_template("pedir.html")
### ruta renderizado de clientes    
@app.route('/clientes.html')
def clientes():
    return render_template("clientes.html")
### ruta renderizado de empleados    
@app.route('/empleados.html')
def empleados():
    return render_template("empleados.html")


app.run(debug=True)