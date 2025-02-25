# Définition des constantes

Dans cette étape, nous allons définir quelques constantes, y compris la couleur du logo et la police de caractères.

```python
MPL_BLUE = '#11557c'

def get_font_properties():
    # La police d'origine est Calibri, si elle n'est pas installée, on utilise
    # Carlito, qui est métriquement équivalent.
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        return matplotlib.font_manager.FontProperties(family='Calibri',
                                                      weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        print('Police d\'origine non trouvée. Passage à Carlito. '
              'Le texte du logo ne sera pas dans la police correcte.')
        return matplotlib.font_manager.FontProperties(family='Carlito',
                                                      weight='bold')
    print('Police d\'origine non trouvée. '
          'Le texte du logo ne sera pas dans la police correcte.')
    return None
```
