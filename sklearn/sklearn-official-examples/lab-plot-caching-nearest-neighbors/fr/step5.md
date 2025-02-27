# Mettre en cache le graphe des plus proches voisins

Dans cette étape, nous allons mettre en cache le graphe des plus proches voisins entre plusieurs ajustements de KNeighborsClassifier en utilisant la propriété de mise en cache des pipelines.

```python
# Notez que nous donnons à `memory` un répertoire pour mettre en cache le calcul du graphe
# qui sera utilisé plusieurs fois lors de la réglage des hyperparamètres du
# classifieur.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
