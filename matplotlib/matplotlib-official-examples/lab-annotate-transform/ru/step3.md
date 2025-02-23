# Создание графика

Теперь мы создадим график с использованием библиотеки `matplotlib.pyplot`. Мы установим пределы по осям x и y и затем построим данные.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```
