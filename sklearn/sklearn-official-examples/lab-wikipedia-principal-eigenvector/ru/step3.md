# Вычисление матрицы смежности

Мы извлечем граф смежности в виде разреженной матрицы в scipy. Переадресации разрешаются сначала. Возвращает X - разреженную матрицу смежности в scipy, redirects - словарь на Python от имен статей к именам статей, и index_map - словарь на Python от имен статей к целым числам Python (индексам статей).

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """Извлечь граф смежности в виде разреженной матрицы в scipy"""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split)!= 4:
            print("игнорируем неправильную строку: " + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] строка: %08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("Вычисление матрицы смежности")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("Преобразование в CSR представление")
    X = X.tocsr()
    print("Преобразование CSR завершено")
    return X, redirects, index_map


# остановиться после 5M ссылок, чтобы можно было работать в RAM
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
