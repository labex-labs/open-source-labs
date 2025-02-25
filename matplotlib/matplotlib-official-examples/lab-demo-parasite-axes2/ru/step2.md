# Создаем основную и паразитные оси

Мы создадим основную ось и две паразитные оси с использованием функций `host_subplot()` и `twinx()`. Функция `host_subplot()` создает основную ось, а функция `twinx()` создает паразитные оси, которые совместно используют ту же ось x, что и основная ось.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
