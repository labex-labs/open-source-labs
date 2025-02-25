# Добавьте аннотацию в виде фигуры

Теперь мы добавим аннотацию в виде фигуры к графику. Следующий код добавит прямоугольник вокруг второй точки данных.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Data Point 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
