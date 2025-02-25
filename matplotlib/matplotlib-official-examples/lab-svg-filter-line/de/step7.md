# SVG lesen und modifizieren

Wir lesen das gespeicherte SVG mit `ET.XMLID()` und fügen die Filterdefinition in den SVG-DOM-Baum ein mit `tree.insert()`. Anschließend greifen wir das SVG-Element mit der angegebenen ID auf und wenden den Schattenfilter an mit `shadow.set()`.

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
