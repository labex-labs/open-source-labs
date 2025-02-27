# Créez le modèle

Ensuite, nous allons créer le modèle de regroupement hiérarchique en utilisant la fonction `AgglomerativeClustering()` du module `sklearn.cluster`.

```python
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
```
