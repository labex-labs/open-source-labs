# Cargar datos

Cargaremos datos del `20newsgroups_dataset`, que comprende alrededor de 18000 publicaciones de grupos de noticias en 20 temas divididos en dos subconjuntos: uno para el entrenamiento y otro para la prueba. Por simplicidad y para reducir el costo computacional, seleccionamos un subconjunto de 7 temas y usamos solo el conjunto de entrenamiento.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "misc.forsale",
    "rec.autos",
    "sci.space",
    "talk.religion.misc",
]

print("Loading 20 newsgroups training data")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} documents - {data_size_mb:.3f}MB")
```
