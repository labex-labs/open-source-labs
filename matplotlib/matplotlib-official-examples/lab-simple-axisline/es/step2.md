# Crear figura y subtrama

A continuación, creamos una figura y agregamos una subtrama con AxesZero. Esto crea una línea de eje con etiquetas de eje x e y, pero sin marcas de graduación ni rejillas.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
