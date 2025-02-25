# Crear datos

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

Creamos los datos para la gráfica. Creamos los valores de `X` e `Y` como arrays con valores espaciados uniformemente de -5 a 5 en incrementos de 0.25. Luego creamos una malla (`meshgrid`) de los valores de `X` e `Y` utilizando `np.meshgrid()`. Utilizamos la malla para calcular los valores de `R`, que es la distancia desde el origen. Luego calculamos los valores de `Z` utilizando la función `sin()` de `R`.
