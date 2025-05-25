# Cálculo da matriz de adjacência

Extrairemos o grafo de adjacência como uma matriz esparsa scipy. Primeiro, os redirecionamentos são resolvidos. Retorna X, a matriz de adjacência esparsa scipy, redirecionamentos como um dicionário Python de nomes de artigos para nomes de artigos e index_map, um dicionário Python de nomes de artigos para inteiros Python (índices de artigos).

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """Extrair o grafo de adjacência como uma matriz esparsa scipy"""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split) != 4:
            print("ignorando linha malformada: " + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] linha: %08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("Calculando a matriz de adjacência")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("Convertendo para representação CSR")
    X = X.tocsr()
    print("Conversão CSR concluída")
    return X, redirects, index_map


# parar após 5M links para tornar possível o trabalho na RAM
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
