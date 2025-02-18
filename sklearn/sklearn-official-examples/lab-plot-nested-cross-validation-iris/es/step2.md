# Definir los hiperparámetros

A continuación, definimos los hiperparámetros que se optimizarán para el clasificador de vectores de soporte. En este caso, optimizamos el parámetro de costo `C` y el coeficiente del kernel `gamma`.

```python
# Set up possible values of parameters to optimize over
p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}
```
