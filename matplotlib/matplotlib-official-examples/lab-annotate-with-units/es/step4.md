# Agregar una anotación de flecha con xy y texto con unidades

En este paso, agregaremos una anotación de flecha a la trama utilizando la función `annotate()`. Proporcionaremos la posición de la flecha, el texto que se mostrará y las propiedades de la flecha. También especificaremos las unidades de medida para la posición y el texto.

```python
ax.annotate('máximo local', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
