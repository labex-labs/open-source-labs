# Datenerzeugung

Wir werden die make_blobs-Funktion aus dem sklearn.datasets-Modul verwenden, um einen synthetischen Datensatz mit drei Clustern zu generieren. Der Datensatz wird aus 750 Proben bestehen, wobei die Clusterstandardabweichung 0,4 beträgt. Wir werden die Daten auch mithilfe des StandardScaler aus dem sklearn.preprocessing-Modul standardisieren.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
