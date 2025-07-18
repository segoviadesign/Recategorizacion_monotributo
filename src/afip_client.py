import os
from datetime import datetime
from pyafipws.wsfev1 import WSFEv1
from pyafipws.wsaa import WSAA


def consultar_facturacion_periodo(cuit, cert_path, key_path, fecha_inicio, fecha_fin):
    print("🧩 Inicializando conexión con AFIP (pyafipws)...")

    if not os.path.exists(cert_path):
        raise FileNotFoundError(f"❌ Certificado no encontrado: {cert_path}")
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"❌ Clave privada no encontrada: {key_path}")

    try:
        # Autenticación WSAA
        wsaa = WSAA()
        wsaa.Cuit = cuit
        wsaa.Autenticar("wsfe", cert_path, key_path)

        if wsaa.Excepcion:
            raise Exception(f"❌ Error WSAA: {wsaa.Excepcion}")

        ta_path = wsaa.ta  # Ruta al archivo TA generado

        # Inicializar WSFE
        wsfe = WSFEv1()
        wsfe.Cuit = int(cuit)
        wsfe.SetTicketAcceso(ta_path)

        # Fechas
        fecha_desde = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_hasta = datetime.strptime(fecha_fin, "%Y-%m-%d")

        # Tipos y puntos de venta
        tipos_cbte = [6, 11, 13]  # Factura B, C, Nota de crédito C
        puntos_venta = [1]
        total = 0.0

        for pv in puntos_venta:
            for tipo in tipos_cbte:
                wsfe.CompTotXRequest = 1000
                ok = wsfe.CompConsultar(pv, tipo, 0)
                if not ok:
                    continue

                ultimo = wsfe.UltimoNroCbte
                for nro in range(1, ultimo + 1):
                    if not wsfe.CompConsultar(pv, tipo, nro):
                        continue

                    fecha_cbte = wsfe.xml_respuesta.findtext(".//CbteFch")
                    if not fecha_cbte:
                        continue

                    fecha_cbte_dt = datetime.strptime(fecha_cbte, "%Y%m%d")
                    if fecha_desde <= fecha_cbte_dt <= fecha_hasta:
                        imp_total = float(wsfe.xml_respuesta.findtext(".//ImpTotal", "0"))
                        total += imp_total

        return total

    except Exception as e:
        print(f"❌ Error al consultar facturación: {e}")
        return 0.0
