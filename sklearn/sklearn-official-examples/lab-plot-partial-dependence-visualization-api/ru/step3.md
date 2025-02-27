# Построение кривых частичной зависимости двух моделей на одном графике

В этом шаге мы построим кривые частичной зависимости двух моделей на одном и том же графике.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

Другой способ сравнить кривые - нарисовать их друг на друге. Здесь мы создаем фигуру с одной строкой и двумя столбцами. оси передаются в функцию `PartialDependenceDisplay.plot` в виде списка, которая нарисует кривые частичной зависимости каждой модели на одной и той же оси. Длина списка осей должна быть равна количеству нарисованных графиков.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` - это numpy массив, содержащий оси, используемые для рисования графиков частичной зависимости. Его можно передать в `mlp_disp`, чтобы получить тот же эффект - нарисовать графики друг на друге. Кроме того, `mlp_disp.figure_` хранит фигуру, что позволяет изменить размер фигуры после вызова `plot`. В этом случае `tree_disp.axes_` имеет два измерения, поэтому `plot` будет показывать только метку y и деления по y на самом левом графике.

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
