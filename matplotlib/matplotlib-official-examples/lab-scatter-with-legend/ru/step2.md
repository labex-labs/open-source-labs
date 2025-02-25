# Создание диаграммы рассеяния с несколькими группами

Мы можем создать диаграмму рассеяния с несколькими группами, пройдя в цикле по каждой группе и создав для нее диаграмму рассеяния. Мы задаем цвет, размер и прозрачность маркеров для каждой группы с использованием параметров `c`, `s` и `alpha` соответственно. Мы также задаем параметр `label` именем группы, которое будет использоваться в легенде.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
