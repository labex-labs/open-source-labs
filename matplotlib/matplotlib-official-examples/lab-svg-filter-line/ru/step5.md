# Задаем пределы осей и сохраняем фигуру

Мы задаем пределы по оси x и оси y и сохраняем фигуру в виде строки байтов в формате SVG с использованием `io.BytesIO()` и `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
