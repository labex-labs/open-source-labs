# Определение примера графика

Мы определяем функцию, которая создает простой линейный график с метками по оси x и y и заголовком.

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
