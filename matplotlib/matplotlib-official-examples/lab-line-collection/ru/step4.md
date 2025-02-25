# Создаем график

Теперь мы можем создать график с использованием `matplotlib` и добавить объект `LineCollection` на график с помощью метода `add_collection` объекта `Axes`.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
