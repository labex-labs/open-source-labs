# Calculer les coefficients d'un Bayesian Ridge avec GridSearch

```python
cv = KFold(2)  # générateur de validation croisée pour la sélection du modèle
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
