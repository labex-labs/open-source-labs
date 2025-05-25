# Adicionar texto aos subplots

Adicionaremos texto a cada subplot usando a função `text`. Usaremos os parâmetros `rotation`, `horizontalalignment`, `verticalalignment` e `rotation_mode` para rotacionar e alinhar o texto. Também usaremos o parâmetro `bbox` para destacar a caixa delimitadora (bounding box) do texto.

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
