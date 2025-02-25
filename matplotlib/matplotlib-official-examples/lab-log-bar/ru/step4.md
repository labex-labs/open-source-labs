# Настройка диаграммы

Мы можем настроить внешний вид нашей диаграммы, добавив метки к осям x и y и установив масштаб оси y в логарифмический.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
