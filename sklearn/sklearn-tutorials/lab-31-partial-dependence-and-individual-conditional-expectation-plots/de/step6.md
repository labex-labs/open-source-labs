# Berechnen von Partial-Dependence-Werten für ein bestimmtes Feature

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# Zeichnen der Partial-Dependence-Werte
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Partial Dependence")
plt.title("Partial Dependence Plot")

plt.show()
```
