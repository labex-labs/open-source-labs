# Создаем вторую группу штриховочных паттернов

Мы создадим вторую группу штриховочных паттернов, повторив каждый паттерн дважды, чтобы увеличить плотность. Мы будем использовать следующий список:

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

Мы будем использовать тот же цикл, что и раньше, чтобы создать прямоугольники.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
