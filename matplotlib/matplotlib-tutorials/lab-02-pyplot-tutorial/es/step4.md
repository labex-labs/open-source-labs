# Graficando con variables categóricas

Matplotlib te permite crear gráficos utilizando variables categóricas. Vamos a crear un gráfico de barras, un diagrama de dispersión y un gráfico de líneas con variables categóricas:

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

Explicación:

- Creamos una lista `names` con tres valores categóricos y una lista `values` que representa sus valores correspondientes.
- Se llama a la función `figure` para crear una nueva figura con un tamaño especificado.
- Utilizamos la función `subplot` para crear una cuadrícula de subgráficos. En este ejemplo, creamos tres subgráficos, cada uno con un tipo de gráfico diferente: gráfico de barras, diagrama de dispersión y gráfico de líneas.
- La función `suptitle` se utiliza para establecer el título superior de la figura.
