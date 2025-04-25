# 添加交互性

我们通过创建一个工具提示来为绘图添加交互性，当鼠标悬停在补丁上时，该工具提示将被打开和关闭。我们通过从 SVG 文件创建一个 XML 树、隐藏工具提示，并为补丁分配 `onmouseover` 和 `onmouseout` 回调来实现这一点。我们还定义了在鼠标悬停在补丁上时将被调用的 `ShowTooltip` 和 `HideTooltip` 函数。

```python
tree, xmlid = ET.XMLID(f.getvalue())
tree.set('onload', 'init(event)')

for i in shapes:
    # 获取形状的索引
    index = shapes.index(i)
    # 隐藏工具提示
    tooltip = xmlid[f'mytooltip_{index:03d}']
    tooltip.set('visibility', 'hidden')
    # 为补丁分配 onmouseover 和 onmouseout 回调。
    mypatch = xmlid[f'mypatch_{index:03d}']
    mypatch.set('onmouseover', "ShowTooltip(this)")
    mypatch.set('onmouseout', "HideTooltip(this)")

# 这是定义 ShowTooltip 和 HideTooltip 函数的脚本。
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

# 将脚本插入文件顶部并保存。
tree.insert(0, ET.XML(script))
ET.ElementTree(tree).write('svg_tooltip.svg')
```
