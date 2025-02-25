# Определяем стили линий

В Matplotlib существуют разные способы определения стилей линий. Мы можем использовать предопределенные стили, такие как 'solid' (прямая), 'dashed' (пунктирная), 'dotted' (точная) и 'dashdot' (пунктирно-прямая). Также можно определить пользовательские стили линий с использованием кортежа тире.

```python
linestyle_str = [
     ('solid', 'solid'),      # То же, что (0, ()) или '-'
     ('dotted', 'dotted'),    # То же, что (0, (1, 1)) или ':'
     ('dashed', 'dashed'),    # То же, что '--'
     ('dashdot', 'dashdot')]  # То же, что '-.'

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),
     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]
```
