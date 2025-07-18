from afip import Afip
from datetime import datetime

# Leer certificados
with open("data/acceso/ssegovia/ssegovia.crt") as f:
    cert = f.read()

with open("data/acceso/ssegovia/ssegovia.key") as f:
    key = f.read()

CUIT = 20263932812

afip = Afip({
    "CUIT": CUIT,
    "cert": cert,
    "key": key,
    "production": True,  # True en producción real
    "service": "wsfe"     # Activamos Web Service Factura Electrónica
})

try:
    # Obtener TA para el servicio
    ta = afip.getServiceTA("wsfe")
    print("✅ Ticket de acceso generado correctamente.")

    # Ahora accedés al servicio con afip.webService
    # Este método depende de la versión de la librería, así que se usa así:
    wsfe = afip.webService

    # Asegurate que esté implementado el método 'get_vouchers' (algunas versiones lo tienen)
    # Este ejemplo asume que sí, si no te paso alternativa
    inicio = "2024-07-01"
    fin = "2025-06-30"

    print(f"📤 Consultando facturas emitidas de {inicio} a {fin}...")

    comprobantes = wsfe.get_vouchers(
        start=inicio,
        end=fin,
        point_of_sale=1,
        document_type="CUIT"
    )

    total = sum(float(c["importe_total"]) for c in comprobantes)
    print(f"📄 Facturas encontradas: {len(comprobantes)}")
    print(f"💰 Total facturado: ${total:,.2f}")

except Exception as e:
    print("❌ Error al conectarse con AFIP:")
    print(e)
