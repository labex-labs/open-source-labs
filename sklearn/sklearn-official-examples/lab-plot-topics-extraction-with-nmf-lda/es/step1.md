# Cargar el Conjunto de Datos

Cargaremos el conjunto de datos 20 newsgroups y lo vectorizaremos. Utilizamos algunas heurísticas para filtrar términos inútiles desde el principio: se eliminan los encabezados, pies de página y respuestas citadas de los mensajes, y se eliminan las palabras comunes en inglés, las palabras que aparecen en solo un documento o en al menos el 95% de los documentos.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Loading dataset...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
