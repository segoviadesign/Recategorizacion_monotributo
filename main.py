from flask import Flask, render_template, request
from src.monotributo import determinar_categoria
from src.afip_client import get_total_facturado
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cuit = "20263932812"  # Leído desde acceso.txt en una implementación posterior
    total = None
    categoria = None

    if request.method == "POST":
        fecha_desde = request.form["fecha_desde"].replace("-", "")
        fecha_hasta = request.form["fecha_hasta"].replace("-", "")
        try:
            total = get_total_facturado(fecha_desde, fecha_hasta)
            categoria = determinar_categoria(total)
        except Exception as e:
            total = 0
            categoria = f"Error: {str(e)}"

    return render_template("index.html", cuit=cuit, total=total, categoria=categoria)

if __name__ == "__main__":
    app.run(debug=True)
