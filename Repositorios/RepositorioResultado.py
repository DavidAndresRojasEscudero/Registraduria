from bson import ObjectId
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getResultadosCandidatos(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getMayorVotacionPorMesa(self):
        query1 = {
                "$group": {
                    "_id": "$candidato",
                    "MayorVotacionPorMesa": {
                        "$max": "$voto"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

    def sumaVotosCandidato(self, id_candidato):
        query1 = {
            "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
            "$group": {
                "_id": "$candidato",
                "totalVotos": {
                    "$sum": "$voto"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)
