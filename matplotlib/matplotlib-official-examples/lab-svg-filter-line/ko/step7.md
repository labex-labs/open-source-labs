# SVG 읽기 및 수정

`ET.XMLID()`를 사용하여 저장된 SVG 를 읽어들이고, `tree.insert()`를 사용하여 SVG DOM 트리에 필터 정의를 삽입합니다. 그런 다음 주어진 ID 를 가진 SVG 요소를 선택하고 `shadow.set()`을 사용하여 그림자 필터를 적용합니다.

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
