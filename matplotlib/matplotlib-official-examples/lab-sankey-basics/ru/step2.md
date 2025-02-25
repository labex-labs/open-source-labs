# Создаем простую диаграмму Санкея

Начнем с создания простой диаграммы Санкея, которая демонстрирует, как использовать класс Sankey.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

Этот код создаст диаграмму Санкея с параметрами по умолчанию, включая метки и ориентации потоков. Результат будет отображаться с заголовком "The default settings produce a diagram like this."
