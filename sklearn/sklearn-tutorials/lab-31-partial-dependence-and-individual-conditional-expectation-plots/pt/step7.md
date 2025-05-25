# Calcular valores de expectativa condicional individual para um recurso específico

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# Plotar os valores de expectativa condicional individual
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("Expectativa Condicional Individual")
plt.title("Gráfico de Expectativa Condicional Individual")

plt.show()
```
