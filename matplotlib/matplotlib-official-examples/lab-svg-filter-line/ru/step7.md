# Чтение и модификация SVG

Мы читаем сохраненный SVG с использованием `ET.XMLID()` и вставляем определение фильтра в дерево DOM SVG с использованием `tree.insert()`. Затем мы выбираем элемент SVG с заданным ID и применяем фильтр тени с использованием `shadow.set()`.

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
