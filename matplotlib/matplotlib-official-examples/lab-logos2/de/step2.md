# Definition von Konstanten

In diesem Schritt definieren wir einige Konstanten, einschließlich der Farbe des Logos und der Schriftart.

```python
MPL_BLUE = '#11557c'

def get_font_properties():
    # Die ursprüngliche Schriftart ist Calibri. Wenn diese nicht installiert ist,
    # greifen wir auf Carlito zurück, die metrisch gleichwertig ist.
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        return matplotlib.font_manager.FontProperties(family='Calibri',
                                                      weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        print('Ursprüngliche Schriftart nicht gefunden. Wechsel zu Carlito. '
              'Der Logotext wird nicht in der richtigen Schriftart erscheinen.')
        return matplotlib.font_manager.FontProperties(family='Carlito',
                                                      weight='bold')
    print('Ursprüngliche Schriftart nicht gefunden. '
          'Der Logotext wird nicht in der richtigen Schriftart erscheinen.')
    return None
```
