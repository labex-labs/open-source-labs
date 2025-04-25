# 为直方图添加交互性

接下来，我们将通过使用 ECMAScript（JavaScript）修改 SVG 代码，为直方图添加交互性。我们将使用`set()`方法为补丁和文本对象添加属性。我们还将创建一个全局变量`container`，用于存储属于每个直方图的补丁 ID。最后，我们将创建一个函数`toggle_hist()`，用于设置每个直方图的所有补丁的可见性属性以及标记本身的不透明度。

```python
from io import BytesIO
import json
import xml.etree.ElementTree as ET

plt.rcParams['svg.fonttype'] = 'none'

# Save SVG in a fake file object
f = BytesIO()
plt.savefig(f, format="svg")

# Create XML tree from the SVG file
tree, xmlid = ET.XMLID(f.getvalue())

# Add attributes to the patch objects
for i, t in enumerate(leg.get_patches()):
    el = xmlid[f'leg_patch_{i}']
    el.set('cursor', 'pointer')
    el.set('onclick', "toggle_hist(this)")

# Add attributes to the text objects
for i, t in enumerate(leg.get_texts()):
    el = xmlid[f'leg_text_{i}']
    el.set('cursor', 'pointer')
    el.set('onclick', "toggle_hist(this)")

# Create script defining the function `toggle_hist`
script = """
<script type="text/ecmascript">
<![CDATA[
var container = %s

function toggle(oid, attribute, values) {
    /* Toggle the style attribute of an object between two values.

    Parameters
    ----------
    oid : str
      Object identifier.
    attribute : str
      Name of style attribute.
    values : [on state, off state]
      The two values that are switched between.
    */
    var obj = document.getElementById(oid);
    var a = obj.style[attribute];

    a = (a == values[0] || a == "")? values[1] : values[0];
    obj.style[attribute] = a;
    }

function toggle_hist(obj) {

    var num = obj.id.slice(-1);

    toggle('leg_patch_' + num, 'opacity', [1, 0.3]);
    toggle('leg_text_' + num, 'opacity', [1, 0.5]);

    var names = container['hist_'+num]

    for (var i=0; i < names.length; i++) {
        toggle(names[i], 'opacity', [1, 0])
    };
    }
]]>
</script>
""" % json.dumps(hist_patches)

# Add a transition effect
css = tree.find('.//{http://www.w3.org/2000/svg}style')
css.text = css.text + "g {-webkit-transition:opacity 0.4s ease-out;" + \
    "-moz-transition:opacity 0.4s ease-out;}"

# Insert the script and save to file
tree.insert(0, ET.XML(script))
ET.ElementTree(tree).write("svg_histogram.svg")
```
