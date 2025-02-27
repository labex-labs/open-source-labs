# Évaluer le regroupement

Pour évaluer les performances de l'algorithme de regroupement K-Means, nous pouvons calculer le score d'inertie. Le score d'inertie mesure la somme des distances entre chaque point de données et le centre de cluster auquel il est assigné. Un score d'inertie plus bas indique un regroupement meilleur.

```python
print("Inertia Score:", kmeans.inertia_)
```
