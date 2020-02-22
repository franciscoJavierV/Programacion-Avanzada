## @imports
from flask import Flask
from flask import request
from flask import render_template
from flaskext.mysql import MySQL
import json
##Primeras instancias de flask y la db

app = Flask(__name__, template_folder="../Front", static_folder="../Front")



###ruta renderizado de index
@app.route('/index.html', methods=['GET'] )
def index(): 
    try:
        nombre = request.args.get('nombre')
        direccion = request.args.get('direccion')
        telefono = request.args.get('telefono')
        id = request.args.get('id/nit')
        tipo = request.args.get('tipo')
        if (nombre != ''):
            return 'Hola ' + nombre
        else:
            return render_template('index.html')
    except:
        return render_template('index.html')
        
 ### ruta renderizado de pedir   
@app.route('/pedir.html')
def pedir():
    try:
        Cliente = request.args.get('Cliente')
        Pastel = request.args.get('Pastel')
        Fecha = request.args.get('Fecha')
        Descripcion = request.args.get('Descripcion')
        tipo = request.args.get('tipo')
        fresa = request.args.get('fresa')
        chocolate = request.args.get('chocolate')        
        if (Cliente != ''):
            return 'Hola ' + Cliente +  '  Hola '+Pastel + ' Hola ' + Descripcion  + ' Hola '+ tipo + ' Hola '+fresa + 'hola' + chocolate
        else:
            return render_template('pedir.html')
    except:
        return render_template('pedir.html')
    

    ### ruta renderizado de clientes    
@app.route('/clientes.html')
def clientes():
    return render_template("clientes.html")
### ruta renderizado de empleados    
@app.route('/empleados.html')
def empleados():
    return render_template("empleados.html")


app.run(debug=True)