# Создаем фигуру и подграфик

Далее создаем фигуру и добавляем подграфик с AxesZero. Это создает ось с метками по осям x и y, но без делений и сетки.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
