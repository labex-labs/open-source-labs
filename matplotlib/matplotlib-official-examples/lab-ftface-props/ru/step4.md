# Выводим дополнительные свойства шрифта

В этом шаге мы выведем дополнительные свойства шрифта, доступные только для масштабируемых лиц.

```python
if font.scalable:
    # глобальная ограничивающая рамка лица (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # количество единиц шрифта, охваченных EM
    print('EM:                 ', font.units_per_EM)
    # подъем в 26,6 единицах
    print('Ascender:           ', font.ascender)
    # опускание в 26,6 единицах
    print('Descender:          ', font.descender)
    # высота в 26,6 единицах
    print('Height:             ', font.height)
    # максимальный горизонтальный сдвиг курсора
    print('Max adv width:      ', font.max_advance_width)
    # то же для вертикального расположения
    print('Max adv height:     ', font.max_advance_height)
    # вертикальное положение подчеркивания
    print('Underline pos:      ', font.underline_position)
    # вертикальная толщина подчеркивания
    print('Underline thickness:', font.underline_thickness)
```
