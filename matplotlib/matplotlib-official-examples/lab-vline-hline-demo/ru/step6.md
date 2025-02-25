# Добавление горизонтальных линий

В этом шаге мы добавим горизонтальные линии на график. Мы будем использовать функцию `hlines` из Matplotlib для рисования горизонтальных линий. Мы нарисуем горизонтальные линии при y = 0,5, y = 2,5 и y = 4,5.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
