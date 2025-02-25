# Personalizar los diagramas de barras

Ahora personalizaremos los diagramas de barras. Crearemos una matriz de colores y utilizaremos el método `bar()` para trazar los diagramas de barras. Estableceremos el parámetro `zdir` en 'y' para proyectar los diagramas de barras sobre los planos del eje y. También estableceremos el parámetro `alpha` en 0,8 para ajustar la transparencia de las barras.

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```
