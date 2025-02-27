# Построение графиков результатов

Последним шагом является построение графиков результатов. Мы будем использовать два подграфика для построения графиков оценок на обучающем и тестовом наборах, а также числа итераций и времени обучения. Для каждого оценщика и критерия остановки мы будем использовать разные стили линий.

```python
# Определяем, что будем отображать
lines = "Критерий остановки"
x_axis = "max_iter"
styles = ["-.", "--", "-"]

# Первый график: оценки на обучающем и тестовом наборах
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["Оценка на обучающем наборе", "Оценка на тестовом наборе"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# Второй график: n_iter и время обучения
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "Время обучения (сек)"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
