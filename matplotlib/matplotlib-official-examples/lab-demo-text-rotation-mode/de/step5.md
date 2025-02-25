# Füge Text zu den Subplots hinzu

Wir werden Text zu jedem Subplot mit der `text`-Funktion hinzufügen. Wir werden die Parameter `rotation` (Drehung), `horizontalalignment` (horizontale Ausrichtung), `verticalalignment` (vertikale Ausrichtung) und `rotation_mode` (Rotationsmodus) verwenden, um den Text zu drehen und auszurichten. Wir werden auch den Parameter `bbox` verwenden, um die Begrenzung des Texts hervorzuheben.

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
