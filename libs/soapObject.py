"""Web services SOAP object."""

from suds.client import Client
__author__ = "Caleb Cipra"
__updated_by__ = "Danilo Toro"
__version__ = "1.0.0"


class SoapObject:

    def __init__(self, wsdl, username='', password=''):
        self.wsdl = wsdl
        self.client = Client(self.wsdl, username=username, password=password)
        self.username = username
        self.password = password

    def getServiceNames(self):
        a = self.client.__str__()
        a = a.replace(" ", "")
        a = a.split("\n")

        lugar = None
        for index, i in enumerate(a, start=0):
            encontro = i.find("Methods")
            if encontro != -1:
                lugar = index
                break

        cuantosSon = a[lugar].replace("Methods(", "")
        cuantosSon = cuantosSon.replace("):", "")
        cuantosSon = eval(cuantosSon)
        lugar = lugar + 1
        cuantosSon = lugar + cuantosSon
        b = a[lugar:cuantosSon]
        c = []
        for each in b:
            where = each.find("(")
            if where != -1:
                each = each[:where]
                c.append(each)
        return c

    def serviceExe(self, serviceName, parameters):
        ejecucionServicio = f"self.client.service.{serviceName}(**{parameters})"
        result = eval(ejecucionServicio)
        # result = getattr(self.client.service, serviceName)(*parameters)
        return result

