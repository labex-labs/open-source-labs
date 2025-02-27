# Évaluez les échantillons

Après avoir ajusté l'estimateur, nous pouvons utiliser la méthode `score_samples` pour calculer la log-vraisemblance des échantillons sous la fonction de densité estimée. Cela nous donnera une mesure de la probabilité de chaque échantillon selon l'estimation de la densité.

```python
scores = kde.score_samples(X)
```
