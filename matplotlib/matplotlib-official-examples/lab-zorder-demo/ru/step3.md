# Установка zorder для делений и сеточных линий

Мы можем использовать метод `set_axisbelow()` или параметр `axes.axisbelow`, чтобы установить `zorder` для делений и сеточных линий.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
