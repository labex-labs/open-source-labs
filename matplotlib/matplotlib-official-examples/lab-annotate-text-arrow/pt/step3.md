# Adicionar uma seta de texto para indicar a direção

Para indicar a direção dos dados, adicionaremos uma seta de texto usando a função `ax.text()` e o parâmetro `bbox` com o `boxstyle` definido como "rarrow".

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```
