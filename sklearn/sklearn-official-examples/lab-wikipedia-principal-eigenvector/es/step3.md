# Calculando la matriz de adyacencia

Extraeremos el gráfico de adyacencia como una matriz dispersa de scipy. Las redirecciones se resuelven primero. Devuelve X, la matriz de adyacencia dispersa de scipy, las redirecciones como un diccionario de Python de nombres de artículo a nombres de artículo, e index_map, un diccionario de Python de nombres de artículo a enteros de Python (índices de artículo).

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """Extraer el gráfico de adyacencia como una matriz dispersa de scipy"""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split)!= 4:
            print("ignorando línea malformada: " + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] línea: %08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("Calculando la matriz de adyacencia")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("Convirtiendo a representación CSR")
    X = X.tocsr()
    print("Conversión CSR realizada")
    return X, redirects, index_map


# detener después de 5M enlaces para poder trabajar en RAM
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
