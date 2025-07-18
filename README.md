# Recategorizacion Monotributo

Herramienta basica para consultar las facturas electronicas emitidas y comparar el total anual con los limites de categorias del Monotributo.

## Instalacion

Se requiere Python 3.8 o superior junto con las dependencias listadas en
`requirements.txt` (`requests` y `pyafipws`).

```bash
pip install -r requirements.txt
```

## Configuracion

Antes de ejecutar el programa deben definirse las siguientes variables de entorno:

- `AFIP_CUIT`: CUIT del contribuyente.
- `AFIP_CERT_PATH`: Ruta al certificado digital (archivo `.crt`).
- `AFIP_KEY_PATH`: Ruta a la clave privada (archivo `.key`).
- `AFIP_WS_URL`: URL del servicio WSFE (opcional, por defecto un servicio dummy).

Estas variables pueden almacenarse en un archivo `.env` que no se incluye en el repositorio.

## Uso

El modulo `AFIPClient` permite consultar las facturas:

```python
from datetime import datetime
from src.afip_client import AFIPClient, sum_invoices_total

client = AFIPClient()
start = datetime(2023, 1, 1)
end = datetime(2023, 12, 31)

invoices = client.get_invoices(start, end)
total = sum_invoices_total(invoices)
print("Ventas del periodo:", total)
```

Luego puede compararse con las categorias definidas en `src/monotributo.py` para saber si corresponde recategorizar.

## Pruebas

Las pruebas unitarias se ejecutan con `pytest`:

```bash
pytest
```
