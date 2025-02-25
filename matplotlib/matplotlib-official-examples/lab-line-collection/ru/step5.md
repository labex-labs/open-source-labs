# Отображаем цвета значениями

Мы также можем отобразить массив значений на цвета с использованием функции `ScalarMappable.set_array`. Мы создадим новый набор данных и новый объект `LineCollection` с параметром `array`, установленным на значения `x`. Затем мы можем использовать метод `colorbar` объекта `Figure`, чтобы добавить цветовую шкалу на график.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
