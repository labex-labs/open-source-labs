# Carregar o Conjunto de Dados

Utilizaremos o conjunto de dados 20 newsgroups, que contém cerca de 18.000 mensagens de grupos de notícias sobre 20 tópicos. Nesta etapa, carregaremos o conjunto de dados e imprimiremos algumas informações básicas sobre ele.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Carregar o conjunto de dados com as cinco primeiras categorias
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

# Imprimir informações sobre o conjunto de dados
print("%d documentos" % len(data.filenames))
print("%d categorias" % len(data.target_names))
```
