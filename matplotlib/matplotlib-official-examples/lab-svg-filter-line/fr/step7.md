# Lire et modifier un SVG

Nous lisons le SVG enregistré à l'aide de `ET.XMLID()` et insérons la définition du filtre dans l'arbre DOM du SVG à l'aide de `tree.insert()`. Nous récupérons ensuite l'élément SVG avec l'ID donné et appliquons le filtre d'ombre à l'aide de `shadow.set()`.

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
