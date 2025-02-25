# Generar puntos de datos de prueba

Generamos un conjunto de puntos de datos de prueba aleatorios, con valores de x e y entre -1 y 1. También generamos un conjunto correspondiente de valores de z utilizando la función `experiment_res` definida en el paso 2.

```python
# User parameters for data test points

# Número de puntos de datos de prueba, probado de 3 a 5000 para subdiv=3
n_test = 200

# Puntos aleatorios
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
