# Definiendo las constantes

En este paso, definiremos algunas constantes, incluyendo el color del logotipo y la fuente.

```python
MPL_BLUE = '#11557c'

def get_font_properties():
    # La fuente original es Calibri, si no está instalada, utilizamos
    # Carlito, que es métricamente equivalente.
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        return matplotlib.font_manager.FontProperties(family='Calibri',
                                                      weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        print('Fuente original no encontrada. Utilizando Carlito como reemplazo. '
              'El texto del logotipo no tendrá la fuente correcta.')
        return matplotlib.font_manager.FontProperties(family='Carlito',
                                                      weight='bold')
    print('Fuente original no encontrada. '
          'El texto del logotipo no tendrá la fuente correcta.')
    return None
```
