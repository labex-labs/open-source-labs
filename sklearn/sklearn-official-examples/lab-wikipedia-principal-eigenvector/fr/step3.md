# Calcul de la matrice d'adjacence

Nous allons extraire le graphe d'adjacence sous forme d'une matrice creuse scipy. Les redirections sont résolues en premier. Renvoie X, la matrice d'adjacence creuse scipy, les redirections sous forme de dictionnaire python de noms d'articles vers des noms d'articles, et index_map un dictionnaire python de noms d'articles vers des entiers python (index d'articles).

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """Extraire le graphe d'adjacence sous forme d'une matrice creuse scipy"""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split)!= 4:
            print("ignorer la ligne malformée : " + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] ligne : %08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("Calcul de la matrice d'adjacence")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("Conversion en représentation CSR")
    X = X.tocsr()
    print("Conversion CSR terminée")
    return X, redirects, index_map


# s'arrêter après 5M liens pour pouvoir travailler en mémoire vive
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
