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
    monkeypatch.setenv('AFIP_CUIT', '12345678901')
    monkeypatch.setenv('AFIP_CERT_PATH', '/tmp/cert.crt')
    monkeypatch.setenv('AFIP_KEY_PATH', '/tmp/key.key')
    client = AFIPClient()
    assert client.cuit == '12345678901'
    assert client.cert_path == '/tmp/cert.crt'
    assert client.key_path == '/tmp/key.key'
    assert client.base_url == 'https://dummy.afip/wsfe'
