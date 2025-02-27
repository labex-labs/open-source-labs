# Zwei informative Merkmale, zwei Cluster pro Klasse

Wir erstellen einen Datensatz mit zwei informativen Merkmalen und zwei Clustern pro Klasse und plotten ihn.

```python
plt.subplot(323)
plt.title("Two informative features, two clusters per class", fontsize="small")
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker="o", c=Y2, s=25, edgecolor="k")
```
