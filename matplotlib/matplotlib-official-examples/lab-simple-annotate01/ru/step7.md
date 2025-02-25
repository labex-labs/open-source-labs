# Размещение аннотаций

Мы можем размещать аннотации с использованием различных систем координат. Следующий код размещает текстовую аннотацию с использованием координат данных, а стрелковую аннотацию - с использованием координат рисунка.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
