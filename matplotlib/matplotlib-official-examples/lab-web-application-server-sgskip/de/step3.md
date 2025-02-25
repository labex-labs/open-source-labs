# Flask-Anwendung erstellen

In diesem Schritt erstellen wir die Flask-Anwendung. Wir definieren eine Route für die Startseite (`"/"`) und eine Funktion, um die Matplotlib-Figur zu generieren und einzubetten.

```python
app = Flask(__name__)

@app.route("/")
def home():
    # Generieren Sie die Figur **ohne die Verwendung von pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Speichern Sie sie in einem temporären Puffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Betten Sie das Ergebnis in die HTML-Ausgabe ein.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
```
