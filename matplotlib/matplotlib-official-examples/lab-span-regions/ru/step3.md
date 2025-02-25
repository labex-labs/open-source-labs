# Создаем график

Теперь мы создадим график с использованием `matplotlib.pyplot`. Мы построим синусоидальную волну и добавим горизонтальную линию при y = 0.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```
