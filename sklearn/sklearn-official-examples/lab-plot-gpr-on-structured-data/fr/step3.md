# Effectuer une régression sur des séquences

Nous pouvons utiliser notre `SequenceKernel` pour effectuer une régression sur des séquences. Nous utiliserons un ensemble de données de 6 séquences et utiliser les 1ère, 2ème, 4ème et 5ème séquences comme ensemble d'entraînement pour effectuer des prédictions sur les 3ème et 6ème séquences.

```python
X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])
Y = np.array([1.0, 1.0, 2.0, 2.0, 3.0, 3.0])

training_idx = [0, 1, 3, 4]
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X[training_idx], Y[training_idx])

plt.figure(figsize=(8, 5))
plt.bar(np.arange(len(X)), gp.predict(X), color="b", label="prédiction")
plt.bar(training_idx, Y[training_idx], width=0.2, color="r", alpha=1, label="entraînement")
plt.xticks(np.arange(len(X)), X)
plt.title("Régression sur des séquences")
plt.legend()
plt.show()
```
