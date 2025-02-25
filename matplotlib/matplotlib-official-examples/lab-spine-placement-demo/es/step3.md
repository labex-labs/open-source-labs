# Definir un método para ajustar las ubicaciones de las espinas

En este paso, definiremos un método que ajuste la ubicación de las espinas de los ejes basado en las ubicaciones de espinas especificadas.

```python
def adjust_spines(ax, spines):
    """
    Ajusta la ubicación de las espinas de los ejes basado en las ubicaciones de espinas especificadas.

    Parámetros:
        ax (Axes): El objeto Axes de Matplotlib para el cual se ajustarán las espinas.
        spines (lista de str): Las ubicaciones de espinas deseadas. Las opciones válidas son 'left', 'right', 'top', 'bottom'.

    Devuelve:
        Ninguno
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # mueve la espina hacia afuera 10 puntos
        else:
            spine.set_color('none')  # no dibuja la espina

    # desactiva las marcas donde no hay espina
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
