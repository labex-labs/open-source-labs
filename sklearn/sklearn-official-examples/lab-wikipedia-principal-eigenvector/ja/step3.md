# 隣接行列の計算

scipy の疎行列として隣接グラフを抽出します。まずリダイレクトを解決します。scipy の疎隣接行列 X と、記事名から記事名への Python 辞書としてのリダイレクト、および記事名から Python の int（記事インデックス）への Python 辞書である index_map を返します。

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """scipy の疎行列として隣接グラフを抽出する"""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split)!= 4:
            print("整形されていない行を無視：" + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] 行：%08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("隣接行列を計算中")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("CSR 表現に変換中")
    X = X.tocsr()
    print("CSR 変換完了")
    return X, redirects, index_map


# 500 万のリンクで停止して RAM 内で作業できるようにする
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
