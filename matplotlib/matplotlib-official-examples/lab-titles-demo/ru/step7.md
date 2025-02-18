# Вертикальная позиция с использованием rcParams

Установите параметры `titley` и `titlepad` объекта `rcParams` для настройки вертикальной позиции заголовка.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
plt.rcParams['axes.titley'] = 1.0
plt.rcParams['axes.titlepad'] = -14
ax.set_title('RCParam Y Positioning')
```
