# Добавляем метки осей и заголовок

Добавим метки осей и заголовок к графику с использованием функций `plt.ylabel`, `plt.yticks`, `plt.xticks` и `plt.title`.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Убыток в ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Убыток по катастрофам')
```
