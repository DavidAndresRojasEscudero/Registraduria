from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):

        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.inscritos = infoMesa["inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)



'''
class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todas las mesas")
        unaMesa = {
            "id": "1",
            "numero": "12",
            "inscritos": "70",
        }
        return [unaMesa]


    def create(self,infoMesa):
        print("Crear una mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__


    def show(self,id):
        print("Mostrando una mesa por id ", id)
        laMesa = {
            "id": id,
            "numero": "12",
            "inscritos": "70",
        }
        return laMesa


    def update(self, id, infoMesa):
        print("Actualizando Candidato con id ", id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__


    def delete(self, id):
        print("Eliminando mesa con id ", id)
        return {"deleted_count":1}
'''