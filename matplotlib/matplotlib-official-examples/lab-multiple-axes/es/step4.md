# Dibujar la curva senoidal

El cuarto paso es dibujar la curva senoidal en la subtrama derecha. Creamos una matriz de ángulos y luego trazamos el seno de cada ángulo. También guardamos el objeto de trazado `sine`, que actualizaremos más adelante en la animación.

```python
sine, = axr.plot(x, np.sin(x))
```
