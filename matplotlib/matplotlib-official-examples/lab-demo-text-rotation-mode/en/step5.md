# Add text to the subplots

We will add text to each subplot using the `text` function. We will use the parameters `rotation`, `horizontalalignment`, `verticalalignment`, and `rotation_mode` to rotate and align the text. We will also use the `bbox` parameter to highlight the bounding box of the text.

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
