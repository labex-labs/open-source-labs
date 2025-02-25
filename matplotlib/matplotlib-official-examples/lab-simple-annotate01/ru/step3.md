# Добавьте текстовую аннотацию

Теперь мы добавим текстовую аннотацию к графику. Следующий код добавит текст "Data Point 1" к первой точке данных.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
