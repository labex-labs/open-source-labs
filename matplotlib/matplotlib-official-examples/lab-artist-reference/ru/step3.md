# Нарисовать фигуры

Теперь мы нарисуем фигуры с использованием Matplotlib, пройдя по списку `shapes` и добавив их на график.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
