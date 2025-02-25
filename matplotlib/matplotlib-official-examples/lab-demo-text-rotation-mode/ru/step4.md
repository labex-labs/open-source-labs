# Создаем подграфики

Теперь мы создадим подграфики с использованием функции `subplots`. Мы создадим сетку подграфиков с одинаковым соотношением сторон и удалим деления по осям x и y. Также добавим вертикальную и горизонтальную линию в центре каждого подграфика, чтобы помочь визуализировать выравнивание.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
