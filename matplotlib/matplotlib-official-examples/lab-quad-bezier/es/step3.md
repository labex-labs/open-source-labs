# Creando el objeto PathPatch

Ahora que tenemos el objeto `Path`, podemos crear el objeto `PathPatch` que se utilizará para dibujar la curva de Bezier en la gráfica. Estableceremos el `facecolor` en `'none'` para que se dibuje solo la curva y no se rellene.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
