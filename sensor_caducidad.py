import json
import sys

from prtg.sensor.result import CustomSensorResult
from prtg.sensor.units import ValueUnit
from six.moves import urllib

json_default = {}

url_web_service = 'http://localhost:7778/caducidadEmpresaDiasAll'

try:
     url_contenido = urllib.request.urlopen(url_web_service)
     parametros = json.loads(url_contenido.read().decode("utf-8"))
except Exception as inst:
     parametros = json_default


# lTiempoCaducidad = parametros["valor"]["lCaducidad"]
# lNombreEmpresa = parametros["valor"]["nombre_empresa"]
  
# print("Nombre Empresa: ", lNombreEmpresa)
# print("Estos son los dias para que caduque el contrato: ", lTiempoCaducidad)

lParametros = parametros["valor"]


if __name__ == "__main__":
   # interpreta el primer parámetro de línea de comando como objeto json
   data = json.loads(sys.argv[1])
   # crear resultado del sensor
   result =  CustomSensorResult("OK")
   # Añadir canal
   for parametros in lParametros:
     result.add_primary_channel(name = parametros["nombre_empresa"], unit = "Count", value = parametros["lCaducidad"], is_float = False)
   print(result.json_result)