from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)


 # base de datos

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.elzxuae.mongodb.net/bd-registraduria?retryWrites=true&w=majority",tlsCAFile=ca)

db = client.test
print(db)

baseDatos = client["bd-registraduria"]
print(baseDatos.list_collection_names())

    # servidor corriendo

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


    # CRUD CANDIDATO

from Controladores.ControladorCandidato import ControladorCandidato

miControladorCandidato = ControladorCandidato()

@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(cedula):
    json=miControladorCandidato.delete(id)
    return jsonify(json)


    # CRUD MESA

from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)


    # CRUD PARTIDO

from Controladores.ControladorPartido import ControladorPartido
miControladorPartido=ControladorPartido()

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


    # CRUD RESULTADOS

from Controladores.ControladorResultado import ControladorResultado
miControladorResultado = ControladorResultado()

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

    #relacion mesas-candidatos a resultados

@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>",methods=['POST'])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/mesas/<string:id_mesa>/candidatos/<string:id_candidato>",methods=['PUT'])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>", methods=['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)


    # Relacion candidato partido

@app.route("/candidatos/<string:id>/partidos/<string:id_partido>", methods = ['PUT'])

def asignarPartidoACandidato(id, id_partido):
    json = miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)


    # Config

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

