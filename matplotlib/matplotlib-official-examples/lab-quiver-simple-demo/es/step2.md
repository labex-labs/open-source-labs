# Crear datos

Necesitamos crear las coordenadas `X` e `Y` usando la función `np.meshgrid()`. Luego, creamos las matrices `U` y `V` que representan los campos vectoriales.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
