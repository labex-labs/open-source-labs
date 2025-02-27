# Вычисляем значения индивидуального условного ожидания для определенной характеристики

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# Строим график значений индивидуального условного ожидания
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("Индивидуальное условное ожидание")
plt.title("График индивидуального условного ожидания")

plt.show()
```
