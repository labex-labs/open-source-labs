# Изменяем последовательность пунктира с использованием `.Line2D.set_dashes()`

Мы можем изменить последовательность пунктира с использованием `.Line2D.set_dashes()`. В этом примере мы изменяем последовательность пунктира для `line1`, чтобы создать шаблон пунктира: 2pt линия, 2pt перерыв, 10pt линия и 2pt перерыв. Мы также задаем стиль окончания штриха 'round' с использованием `line1.set_dash_capstyle()`.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
