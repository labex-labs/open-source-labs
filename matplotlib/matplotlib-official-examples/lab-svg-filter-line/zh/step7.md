# 读取并修改SVG

我们使用 `ET.XMLID()` 读取保存的SVG，并使用 `tree.insert()` 将滤镜定义插入到SVG DOM树中。然后，我们通过给定的ID获取SVG元素，并使用 `shadow.set()` 应用阴影滤镜。

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
