# Определение констант

В этом шаге мы определим некоторые константы, включая цвет логотипа и шрифт.

```python
MPL_BLUE = '#11557c'

def get_font_properties():
    # Исходный шрифт - Calibri, если он не установлен, мы переходим
    # к Carlito, который метрически эквивалентен.
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        return matplotlib.font_manager.FontProperties(family='Calibri',
                                                      weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        print('Исходный шрифт не найден. Переходим к Carlito. '
              'Текст логотипа не будет отображаться в правильном шрифте.')
        return matplotlib.font_manager.FontProperties(family='Carlito',
                                                      weight='bold')
    print('Исходный шрифт не найден. '
          'Текст логотипа не будет отображаться в правильном шрифте.')
    return None
```
