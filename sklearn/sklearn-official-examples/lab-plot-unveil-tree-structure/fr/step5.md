# Déterminer les nœuds communs pour un groupe d'échantillons

Pour un groupe d'échantillons, nous pouvons déterminer les nœuds communs que les échantillons traversent en utilisant la méthode `decision_path` et la méthode `toarray` pour convertir la matrice d'indicateurs en un tableau dense.

```python
sample_ids = [0, 1]
# tableau booléen indiquant les nœuds traversés par les deux échantillons
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# obtenir les identifiants de nœuds en utilisant leur position dans le tableau
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nLes échantillons suivants {samples} partagent le ou les nœuds {nodes} dans l'arbre.".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("Ceci représente {prop}% de tous les nœuds.".format(prop=100 * len(common_node_id) / n_nodes))
```
