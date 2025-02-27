# Datenvisualisierung

In diesem Schritt werden wir den rauschenden Trainingsdatensatz zusammen mit dem erwarteten Signal visualisieren.

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
