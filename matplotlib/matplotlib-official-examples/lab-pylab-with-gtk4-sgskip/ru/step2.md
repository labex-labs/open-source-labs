# Создаем фигуру и графики

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

Мы создаем фигуру с двумя подграфиками и наносим на них две группы данных. Также добавляем легенду к графикам.
