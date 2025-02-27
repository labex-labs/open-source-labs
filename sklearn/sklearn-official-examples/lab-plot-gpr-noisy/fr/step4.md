# Visualisation des données

Dans cette étape, nous allons visualiser l'ensemble de données d'entraînement bruité ainsi que le signal attendu.

```python
plt.plot(X, y, label="Expected signal")
plt.scatter(
    x=X_train[:, 0],
    y=y_train,
    color="black",
    alpha=0.4,
    label="Observations",
)
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
