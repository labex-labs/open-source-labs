# Bestimme gemeinsame Knoten für eine Gruppe von Proben

Für eine Gruppe von Proben können wir die gemeinsamen Knoten bestimmen, durch die die Proben gehen, indem wir die `decision_path`-Methode und die `toarray`-Methode verwenden, um die Indikatormatrix in ein dichtes Array umzuwandeln.

```python
sample_ids = [0, 1]
# boolescher Array, das die Knoten angibt, durch die beide Proben gehen
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# erhalte Knoten-IDs mithilfe der Position im Array
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nDie folgenden Proben {samples} teilen die Knoten {nodes} im Baum.".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("Dies entspricht {prop}% aller Knoten.".format(prop=100 * len(common_node_id) / n_nodes))
```
