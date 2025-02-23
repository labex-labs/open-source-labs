# Agregar una anotación de flecha con unidades mixtas

En este paso, agregaremos otra anotación de flecha a la trama utilizando la función `annotate()`. Proporcionaremos la posición de la flecha, el texto que se mostrará y las propiedades de la flecha. También combinaremos unidades de medida para la posición y usaremos la fracción de los ejes para el texto.

```python
ax.annotate('máximo local', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
