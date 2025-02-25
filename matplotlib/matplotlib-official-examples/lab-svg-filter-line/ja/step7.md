# SVG を読み込んで変更する

保存した SVG を `ET.XMLID()` を使って読み込み、`tree.insert()` を使って SVG DOM ツリーにフィルタ定義を挿入します。その後、与えられた ID の SVG 要素を取得し、`shadow.set()` を使って影のフィルタを適用します。

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
