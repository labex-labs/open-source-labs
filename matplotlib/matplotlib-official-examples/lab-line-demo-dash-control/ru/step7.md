# Задаем другие атрибуты пунктира с использованием соответствующих методов

Другие атрибуты пунктира также можно задать с использованием соответствующих методов, таких как `~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()` и `~.Line2D.set_gapcolor()`. В этом примере мы будем использовать параметры `dashes` и `gapcolor` для задания последовательности пунктиров и чередующегося цвета для `line3`.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
