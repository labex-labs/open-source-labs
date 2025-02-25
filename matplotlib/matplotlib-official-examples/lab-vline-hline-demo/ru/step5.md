# Добавление вертикальных линий

В этом шаге мы добавим вертикальные линии на график. Мы будем использовать функцию `vlines` из Matplotlib для рисования вертикальных линий. Также мы будем использовать параметр `transform`, чтобы установить, что координаты y будут масштабироваться от 0 до 1. Мы нарисуем две вертикальные линии при x = 1 и x = 2.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
