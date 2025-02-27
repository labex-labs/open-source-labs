# Вычисляем значения частичной зависимости для определенной характеристики

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# Строим график значений частичной зависимости
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Частичная зависимость")
plt.title("График частичной зависимости")

plt.show()
```
