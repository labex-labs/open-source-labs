# Cargar el conjunto de datos

Utilizaremos el conjunto de datos 20 newsgroups, que contiene alrededor de 18.000 publicaciones de grupos de noticias sobre 20 temas. En este paso, cargaremos el conjunto de datos y mostraremos algunas información básica sobre él.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Cargar el conjunto de datos con las primeras cinco categorías
data = fetch_20newsgroups(
    subset="train",
    categories=[
        "alt.atheism",
        "comp.graphics",
        "comp.os.ms-windows.misc",
        "comp.sys.ibm.pc.hardware",
        "comp.sys.mac.hardware",
    ],
)

# Mostrar información sobre el conjunto de datos
print("%d documentos" % len(data.filenames))
print("%d categorías" % len(data.target_names))
```
