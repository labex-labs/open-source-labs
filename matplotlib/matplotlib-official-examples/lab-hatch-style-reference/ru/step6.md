# Создаем третью группу штриховочных паттернов

Мы создадим третью группу штриховочных паттернов, комбинируя два паттерна, чтобы создать новый. Мы будем использовать следующий список:

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

Мы будем использовать тот же цикл, что и раньше, чтобы создать прямоугольники.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
