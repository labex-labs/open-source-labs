# Crear la aplicación Flask

En este paso, crearemos la aplicación Flask. Definiremos una ruta para la página de inicio (`"/"`) y una función para generar e incrustar la figura de Matplotlib.

```python
app = Flask(__name__)

@app.route("/")
def home():
    # Generar la figura **sin usar pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Guardarla en un búfer temporal.
    buf = BytesIO()
    fig.savefig(buf, formato="png")
    # Incrustar el resultado en la salida html.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
```
