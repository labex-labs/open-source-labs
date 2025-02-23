# Anotar la gráfica

Ahora, anotaremos la gráfica agregando una flecha que apunte a una coordenada específica. En este ejemplo, agregaremos una flecha que apunte al máximo local de la función coseno.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

La función `ax.annotate()` toma varios argumentos. El primer argumento es el texto que se mostrará en la gráfica. El argumento `xy` especifica las coordenadas del punto que queremos anotar. El argumento `xytext` especifica las coordenadas del texto. El argumento `arrowprops` es un diccionario que especifica las propiedades de la flecha.
