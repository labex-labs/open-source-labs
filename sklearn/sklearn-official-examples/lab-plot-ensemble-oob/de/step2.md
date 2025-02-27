# Erzeugen eines binären Klassifizierungsdatensatzes

Als nächstes werden wir einen binären Klassifizierungsdatensatz mit der Funktion `make_classification` von scikit-learn erzeugen. Mit dieser Funktion können wir die Anzahl der Proben, Merkmale, Cluster pro Klasse und informativen Merkmale angeben. Wir werden einen festen Zufallszustandswert verwenden, um die Reproduzierbarkeit zu gewährleisten.

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```
