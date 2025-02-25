# Gráfico de dispersión

También podemos crear un gráfico de dispersión para mostrar la relación entre dos variables categóricas. En este caso, usaremos los mismos datos de frutas y agregaremos algo de ruido aleatorio a las cantidades para crear una segunda variable.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
