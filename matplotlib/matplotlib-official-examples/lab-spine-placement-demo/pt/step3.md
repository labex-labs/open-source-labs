# Definir um método para ajustar as localizações dos eixos (spines)

Nesta etapa, definiremos um método que ajusta a localização dos eixos (spines) com base nas localizações especificadas.

```python
def adjust_spines(ax, spines):
    """
    Ajusta a localização dos eixos (spines) com base nas localizações especificadas.

    Parâmetros:
        ax (Axes): O objeto Axes do Matplotlib para ajustar os eixos (spines).
        spines (lista de str): As localizações desejadas dos eixos (spines). Opções válidas são 'left', 'right', 'top', 'bottom'.

    Retorna:
        None
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # move the spine outward by 10 points
        else:
            spine.set_color('none')  # don't draw the spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
