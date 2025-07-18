from src.afip_client import consultar_facturacion_periodo

if __name__ == "__main__":
    CUIT = "20263932812"
    CERT_PATH = "data/acceso/ssegovia/ssegovia.crt"
    KEY_PATH = "data/acceso/ssegovia/ssegovia.key"
    WS = "wsfe"

    FECHA_INICIO = "2024-07-01"
    FECHA_FIN = "2025-06-30"

    total = consultar_facturacion_periodo(CUIT, CERT_PATH, KEY_PATH, FECHA_INICIO, FECHA_FIN)
    print(f"Total facturado entre {FECHA_INICIO} y {FECHA_FIN}: ${total:.2f}")