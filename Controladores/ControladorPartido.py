from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):

        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)

'''
class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los partidos")
        unPartido = {
            "id": "1",
            "nombre": "polo",
            "lema": "equidad",
        }
        return [unPartido]


    def create(self,infoPartido):
        print("Crear una mesa")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__


    def show(self,id):
        print("Mostrando un partido por id ", id)
        elPartido = {
            "id": id,
            "nombre": "polo",
            "lema": "equidad",
        }
        return elPartido


    def update(self, id, infoPartido):
        print("Actualizando partido con id ", id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__


    def delete(self, id):
        print("Eliminando partido con id ", id)
        return {"deleted_count":1}
'''