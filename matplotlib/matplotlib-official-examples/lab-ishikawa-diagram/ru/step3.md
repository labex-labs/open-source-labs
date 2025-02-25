# Создание鱼骨图 (диаграммы рыбы)

Теперь мы создадим鱼骨图 (диаграмму рыбы). Начнем с создания объекта фигуры и оси.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Далее установим пределы по осям x и y и отключим оси.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
