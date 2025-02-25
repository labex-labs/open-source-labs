# Créer l'application Flask

Dans cette étape, nous allons créer l'application Flask. Nous allons définir une route pour la page d'accueil (`"/"`) et une fonction pour générer et intégrer la figure Matplotlib.

```python
app = Flask(__name__)

@app.route("/")
def home():
    # Générer la figure **sans utiliser pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # L'enregistrer dans un tampon temporaire.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Intégrer le résultat dans la sortie html.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
```
