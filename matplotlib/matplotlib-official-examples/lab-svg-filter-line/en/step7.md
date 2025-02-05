# Read and Modify SVG

We read in the saved SVG using `ET.XMLID()` and insert the filter definition in the SVG DOM tree using `tree.insert()`. We then pick up the SVG element with the given ID and apply the shadow filter using `shadow.set()`.

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
