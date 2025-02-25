# Добавляем текст в подграфики

Мы добавим текст в каждый подграфик с использованием функции `text`. Мы будем использовать параметры `rotation` (поворот), `horizontalalignment` (горизонтальное выравнивание), `verticalalignment` (вертикальное выравнивание) и `rotation_mode` (режим вращения) для вращения и выравнивания текста. Также мы будем использовать параметр `bbox` для выделения ограничивающего прямоугольника текста.

```python
kw = (
    {} if mode == "default" else
    {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}
)

texts = {}

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        tx = ax.text(0.5, 0.5, "Tpg",
                     size="x-large", rotation=40,
                     horizontalalignment=ha, verticalalignment=va,
                     rotation_mode=mode, **kw)
        texts[ax] = tx
```
