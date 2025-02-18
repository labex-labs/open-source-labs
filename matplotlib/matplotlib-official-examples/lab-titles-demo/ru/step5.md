# Верхний заголовок

Создайте график с заголовком сверху с помощью функции `subplots()` и функции `set_xlabel()`.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```
