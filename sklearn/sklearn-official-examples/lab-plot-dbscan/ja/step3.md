# DBSCANの計算

sklearn.clusterモジュールのDBSCANクラスを使ってクラスタを計算します。epsパラメータを0.3に、min_samplesパラメータを10に設定します。DBSCANによって割り当てられたラベルにはlabels属性を使ってアクセスできます。ノイズのサンプルには-1のラベルが付けられます。また、クラスタの数とノイズポイントの数を計算します。

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
```
