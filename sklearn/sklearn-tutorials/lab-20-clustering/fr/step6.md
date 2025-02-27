# Évaluer le clustering

Pour évaluer les résultats du clustering, nous pouvons calculer l'inertie des clusters, qui représente la somme des distances au carré des échantillons à leur centre de cluster le plus proche.

```python
# Calculate the inertia of the clusters
inertia = kmeans.inertia_
print("Inertia:", inertia)
```
