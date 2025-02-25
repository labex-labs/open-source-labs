# Добавляем интерактивность

Добавляем интерактивность к графику, создавая подсказку, которая будет включаться и выключаться при наведении курсора на фигуры. Для этого создаем XML-дерево из SVG-файла, скрываем подсказки и назначаем вызовы `onmouseover` и `onmouseout` для фигур. Также определяем функции `ShowTooltip` и `HideTooltip`, которые будут вызываться при наведении курсора на фигуры.

```python
tree, xmlid = ET.XMLID(f.getvalue())
tree.set('onload', 'init(event)')

for i in shapes:
    # Получаем индекс фигуры
    index = shapes.index(i)
    # Скрываем подсказки
    tooltip = xmlid[f'mytooltip_{index:03d}']
    tooltip.set('visibility', 'hidden')
    # Назначаем вызовы onmouseover и onmouseout для фигур.
    mypatch = xmlid[f'mypatch_{index:03d}']
    mypatch.set('onmouseover', "ShowTooltip(this)")
    mypatch.set('onmouseout', "HideTooltip(this)")

# Это скрипт, определяющий функции ShowTooltip и HideTooltip.
script = """
    <script type="text/ecmascript">
    <![CDATA[

    function init(event) {
        if ( window.svgDocument == null ) {
            svgDocument = event.target.ownerDocument;
            }
        }

    function ShowTooltip(obj) {
        var cur = obj.id.split("_")[1];
        var tip = svgDocument.getElementById('mytooltip_' + cur);
        tip.setAttribute('visibility', "visible")
        }

    function HideTooltip(obj) {
        var cur = obj.id.split("_")[1];
        var tip = svgDocument.getElementById('mytooltip_' + cur);
        tip.setAttribute('visibility', "hidden")
        }

    ]]>
    </script>
    """

# Вставляем скрипт в начало файла и сохраняем его.
tree.insert(0, ET.XML(script))
ET.ElementTree(tree).write('svg_tooltip.svg')
```
