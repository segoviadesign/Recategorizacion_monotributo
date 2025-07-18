import importlib
from src.afip_client import AFIPClient


def test_modules_importable():
    modules = [
        'src.afip_client',
        'src.monotributo',
        'src.requests',
    ]
    for mod in modules:
        importlib.import_module(mod)


def test_afip_client_env_vars(monkeypatch):
    monkeypatch.setenv('AFIP_CUIT', '20263932812')
    monkeypatch.setenv('AFIP_CERT_PATH', '/data/acceso/ssegovia/facturacion_75e783404c7b5bfc.crt')
    monkeypatch.setenv('AFIP_KEY_PATH', '/data/acceso/ssegovia/ssegovia.key')
    client = AFIPClient()
    assert client.cuit == '20263932812'
    assert client.cert_path == '/data/acceso/ssegovia/facturacion_75e783404c7b5bfc.crt'
    assert client.key_path == '/data/acceso/ssegovia/ssegovia.key'
    assert client.base_url == 'https://dummy.afip/wsfe'
