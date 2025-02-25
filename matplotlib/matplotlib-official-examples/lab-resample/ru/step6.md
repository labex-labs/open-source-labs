# Создание графика

Мы создадим график с использованием Matplotlib. Создадим экземпляр `d` класса `DataDisplayDownsampler` с использованием xdata и ydata. Создадим фигуру и ось с использованием функции subplots. Свяжем линию и выключим автоматическую шкалирование. Подключимся для изменения пределов просмотра, установим пределы по оси x и покажем график.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
