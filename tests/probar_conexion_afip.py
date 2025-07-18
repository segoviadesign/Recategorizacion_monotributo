from afip import Afip

# CUIT vinculado al certificado
CUIT = 20263932812

afip = Afip({
  "CUIT": CUIT,
  "cert": "data/acceso/ssegovia/ssegovia.crt",
  "key": "data/acceso/ssegovia/ssegovia.key"
})


# URL al archivo WSDL de test
#
# Esta URL la podes encontrar en el manual del web service
WSDL_TEST = "https://fwshomo.afip.gov.ar/wsct/CTService?wsdl"

# URL al archivo WSDL de produccion
#
# Esta URL la podes encontrar en el manual del web service
WSDL = "https://serviciosjava.afip.gob.ar/wsct/CTService?wsdl"

# URL del Web service de produccion
#
# Esta URL la podes encontrar en el manual del web service
URL = "https://serviciosjava.afip.gob.ar/wsct/CTService"

# URL del Web service de test
#
# Esta URL la podes encontrar en el manual del web service
URL_TEST = "https://fwshomo.afip.gov.ar/wsct/CTService"

# Seterar en true si el web service requiere usar soap v1.2
#
# Si no estas seguro de que necesita v1.2 proba con ambas opciones
soapV1_2 = False

# Nombre del web service.
#
# El nombre por el cual se llama al web service en ARCA.
# Esto lo podes encontrar en el manual correspondiente.
# Por ej. el de factura electronica se llama "wsfe", el de
# comprobantes T se llama "wsct"
servicio = "wsfe"

# A partir de aca ya no debes cambiar ninguna variable

# Preparamos las opciones para el web service
options = {
  "WSDL": WSDL,
  "WSDL_TEST": WSDL_TEST,
  "URL": URL,
  "URL_TEST": URL_TEST,
  "soapV1_2": soapV1_2
}

# Creamos el web service
genericWebService = afip.webService(servicio, options)






# Obtenemos el Token Authorizataion
ta = genericWebService.getTokenAuthorization()

# Preparamos los datos que nos pide el web service
#
# Este ejemplo es especifico para el wsct. En el manual
# del web service que quieras utilizar encontraras que
# datos requiere cada metodo
data = {
  "authRequest": {
    "token": ta["token"],
    "sign": ta["sign"],
    "cuitRepresentada": afip.CUIT
  },
  "codigoTipoComprobante": 195,
  "numeroPuntoVenta": 3
}

try:
  # Ejecutamos la request al web service
  #
  # consultarUltimoComprobanteAutorizado es un metodo
  # de wsct, esto debes cambiarlo por el metodo que
  # quieras utilizar
  result = genericWebService.executeRequest("consultarUltimoComprobanteAutorizado", data)['consultarUltimoComprobanteAutorizadoReturn']

  if result.get("arrayErrores"):

    # Checkeamos si devolvio error en el resultado.
    #
    # arrayErrores es especifico de este web service.
    # Esto deberas adaptarlo al web service que estes integrando
    err = result["arrayErrores"]["codigoDescripcion"][0] if type(result["arrayErrores"]["codigoDescripcion"]) in (tuple, list) else result["arrayErrores"]["codigoDescripcion"]

    raise Exception("(%s) %s" % (err["codigo"], err["descripcion"])) 

  # Mostramos el resultado
  print(result)

except Exception as e:
  # Mostramos el error
  print(e)
