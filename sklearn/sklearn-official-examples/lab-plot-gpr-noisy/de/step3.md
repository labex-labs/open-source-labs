# Hinzufügen von Rauschen

In diesem Schritt werden wir dem erzeugten Datensatz etwas Rauschen hinzufügen, um einen realitätsnäheren Trainingsdatensatz zu erstellen.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
