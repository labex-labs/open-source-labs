# Выборочное выделение горизонтальных областей по всей оси

Тот же механизм выбора можно применить для заполнения всей вертикальной высоты оси. Чтобы быть независимыми от ограничений по оси y, мы добавляем преобразование, которое интерпретирует значения x в координатах данных, а значения y в координатах оси. Следующий пример выделяет области, в которых данные по оси y выше заданного порога.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
