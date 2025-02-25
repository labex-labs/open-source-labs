# Создание многоугольника интерактивно

Для создания многоугольника интерактивно нам нужно создать объект `Figure` и объект `Axes`. Затем мы можем создать объект `PolygonSelector` и добавить вершины в него, щелкая по графику. Мы также можем использовать клавиши `shift` и `ctrl` для перемещения вершин.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```
