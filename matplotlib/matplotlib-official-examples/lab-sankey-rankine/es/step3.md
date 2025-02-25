# Crear la figura y los ejes

Crearemos un objeto de figura y le agregaremos un único conjunto de ejes. También estableceremos el título de la gráfica.

```python
fig = plt.figure(figsize=(8, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Rankine Power Cycle: Example 8.6 from Moran and "
                     "Shapiro\n\x22Fundamentals of Engineering Thermodynamics "
                     "\x22, 6th ed., 2008")
```
