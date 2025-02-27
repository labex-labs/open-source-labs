# Création des poids d'échantillonnage

Nous allons créer deux ensembles de poids d'échantillonnage. Le premier ensemble de poids d'échantillonnage sera constant pour tous les points, et le second ensemble de poids d'échantillonnage sera plus élevé pour certains points aberrants.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
