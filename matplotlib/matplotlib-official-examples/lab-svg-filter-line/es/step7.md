# Leer y modificar SVG

Leemos el SVG guardado utilizando `ET.XMLID()` e insertamos la definición del filtro en el árbol DOM del SVG utilizando `tree.insert()`. Luego, recuperamos el elemento SVG con el ID dado y aplicamos el filtro de sombra utilizando `shadow.set()`.

```python
tree, xmlid = ET.XMLID(f.getvalue())

tree.insert(0, ET.XML(filter_def))

for l in [l1, l2]:
    shadow = xmlid[l.get_label() + "_shadow"]
    shadow.set("filter", 'url(#dropshadow)')

fn = "svg_filter_line.svg"
print(f"Guardando '{fn}'")
ET.ElementTree(tree).write(fn)
```
