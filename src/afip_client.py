from pyafipws.wsfev1 import WSFEv1
from datetime import datetime

def get_total_facturado(fecha_desde: str, fecha_hasta: str) -> float:
    print("🧩 Inicializando conexión con AFIP (testing)...")
    ws = WSFEv1()
    ws.LanzarTesting = False
    ws.URLWSAA = "https://wswhomo.afip.gov.ar/wsfe/service.asmx"  # homologación explícita
    ws.Cuit = 20263932812

    ws.cert = "data/acceso/ssegovia/ssegovia.crt"
    ws.key = "data/acceso/ssegovia/ssegovia.key"

    try:
        ws.SetTicketAcceso("wsfe")
    except Exception as e:
        print("❌ Error al generar Ticket de Acceso:")
        print(f"Mensaje: {str(e)}")
        if hasattr(ws, "xml_request"):
            print("📝 XML enviado:\n", ws.xml_request)
        if hasattr(ws, "xml_response"):
            print("📨 XML recibido:\n", ws.xml_response)
        raise e

    punto_venta = 1
    tipo_cbte = 6
    ult = ws.CompUltimoAutorizado(punto_venta, tipo_cbte)
    if not ult:
        raise Exception(f"❌ Error obteniendo último comprobante autorizado: {ws.ErrMsg}")

    total = 0.0
    print(f"📦 Consultando comprobantes desde el 1 hasta el {ult}...")

    for nro in range(1, ult + 1):
        if ws.CompConsultar(punto_venta, tipo_cbte, nro):
            fecha_cbte = ws.Resultado["cbte_fch"]
            if fecha_desde <= fecha_cbte <= fecha_hasta:
                importe = float(ws.Resultado["imp_total"])
                total += importe
                print(f"✅ Nro {nro} - Fecha: {fecha_cbte} - Importe: {importe}")
        else:
            print(f"⚠️ Error consultando comprobante {nro}: {ws.ErrMsg}")

    print(f"💰 Total facturado entre {fecha_desde} y {fecha_hasta}: ${total:,.2f}")
    return total
