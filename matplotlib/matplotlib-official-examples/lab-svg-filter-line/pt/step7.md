# Ler e Modificar SVG

Lemos o SVG salvo usando `ET.XMLID()` e inserimos a definição do filtro na árvore DOM do SVG usando `tree.insert()`. Em seguida, selecionamos o elemento SVG com o ID fornecido e aplicamos o filtro de sombra usando `shadow.set()`.

```python
tree, xmlid = ET.XMLID(f.getvalue())

tree.insert(0, ET.XML(filter_def))

for l in [l1, l2]:
    shadow = xmlid[l.get_label() + "_shadow"]
    shadow.set("filter", 'url(#dropshadow)')

fn = "svg_filter_line.svg"
print(f"Saving '{fn}'")
ET.ElementTree(tree).write(fn)
```
