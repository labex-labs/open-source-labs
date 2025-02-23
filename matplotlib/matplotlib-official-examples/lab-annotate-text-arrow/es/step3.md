# Agregar una flecha de texto para indicar la dirección

Para indicar la dirección de los datos, agregaremos una flecha de texto utilizando la función `ax.text()` y el parámetro `bbox` con el `boxstyle` establecido en "rarrow".

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Dirección", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```
