# Berechnung der Adjazenzmatrix

Wir werden den Adjazenzgraphen als scipy sparse Matrix extrahieren. Zuerst werden die Umleitungen aufgelöst. Gibt zurück X, die scipy sparse Adjazenzmatrix, Umleitungen als Python-Dictionary von Artikelnamen zu Artikelnamen und index_map ein Python-Dictionary von Artikelnamen zu Python-Int (Artikelindizes).

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """Extrahiert den Adjazenzgraphen als scipy sparse Matrix"""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split)!= 4:
            print("Ignoriere fehlerhafte Zeile: " + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] Zeile: %08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("Berechne die Adjazenzmatrix")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("Konvertiere in CSR-Repräsentation")
    X = X.tocsr()
    print("CSR-Konvertierung abgeschlossen")
    return X, redirects, index_map


# Stoppe nach 5M Links, um es möglich zu machen, im Arbeitsspeicher zu arbeiten
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
