from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()


    # Asignacion mesa y candidato a resultado

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__


    #Modificación de resultado (mesa y candidato)

    def update(self, id,infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.voto = infoResultado["voto"]
        laMesa =Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    #QUERY

    #obtener resultados
    def resultadosCandidatos(self, id_candidato):
        return self.repositorioResultado.getResultadosCandidatos(id_candidato)

    #Obtener votacion mas altas por Mesa

    def votacionMasAltaPorMesa(self):
        return self.repositorioResultado.getMayorVotacionPorMesa()

    #Obtener suma de votos

    def sumaVotosCandidato(self,id_candidato):
        return self.repositorioResultado.sumaVotosCandidato(id_candidato)




'''
class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los resultados")
        resMesa = {
            "id": "1",
            "mesa": "8",
            "id_partido": "12",

        }
        return [resMesa]

def show(self, id):
    print("Mostrando resultados por id ", id)
    result = {
        "id": id,
        "mesa": "8",
        "partido": "polo",
    }
    return result 
'''