# Visualiser l'ensemble de données

Nous allons maintenant visualiser l'ensemble de données à l'aide de matplotlib. Nous allons tracer les valeurs de X en fonction des valeurs de y.

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
