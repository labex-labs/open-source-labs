# Определение класса ItemProperties

Далее мы определяем класс `ItemProperties`, который будет использоваться для настройки свойств каждого пункта меню. Мы можем установить размер шрифта, цвет метки, цвет фона и значение альфа для каждого пункта с использованием этого класса.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
