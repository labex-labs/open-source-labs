# Dibujar el círculo y el punto inicial

El tercer paso es dibujar el círculo y el punto inicial en la subtrama izquierda. Creamos una matriz de ángulos para generar el círculo y luego trazamos el seno y el coseno de cada ángulo. También trazamos un solo punto en el origen.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```
