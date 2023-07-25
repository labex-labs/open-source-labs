# Matplotlib SVG Tooltip Lab

## Introduction

This lab is a step-by-step tutorial on how to create a tooltip that will show up when hovering over a matplotlib patch. We will create the tooltip in matplotlib and simply toggle its visibility on when hovering over the patch. This approach provides total control over the tooltip placement and appearance, at the expense of more code up front.

## Steps

### Step 1: Create the patches

We first create patches to which tooltips will be assigned.

```python
rect1 = plt.Rectangle((10, -20), 10, 5, fc='blue')
rect2 = plt.Rectangle((-20, 15), 10, 5, fc='green')

shapes = [rect1, rect2]
labels = ['This is a blue rectangle.', 'This is a green rectangle']
```

### Step 2: Add patches and tooltip annotations

We then add the patches and tooltip annotations to the plot. The tooltip annotations are created using the `annotate` method. We set the `xy` parameter to the coordinates of the patch and `xytext` to `(0, 0)` to position the tooltip directly over the patch. We also set the `textcoords` parameter to `'offset points'` to align the tooltip with the patch. We set the `color` parameter to `'w'` to make the text white, `ha` to `'center'` to center the text horizontally, `fontsize` to `8` to set the font size, and `bbox` to set the style of the tooltip box.

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1, .1, .1, .92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```

### Step 3: Save the figure as SVG

We save the figure in a fake file object using the `BytesIO` class and the `savefig` method.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```

### Step 4: Add interactivity

We add interactivity to the plot by creating a tooltip that will be toggled on and off when hovering over the patches. We do this by creating an XML tree from the SVG file, hiding the tooltips, and assigning `onmouseover` and `onmouseout` callbacks to the patches. We also define the `ShowTooltip` and `HideTooltip` functions that will be called when hovering over the patches.

```python
tree, xmlid = ET.XMLID(f.getvalue())
tree.set('onload', 'init(event)')

for i in shapes:
    # Get the index of the shape
    index = shapes.index(i)
    # Hide the tooltips
    tooltip = xmlid[f'mytooltip_{index:03d}']
    tooltip.set('visibility', 'hidden')
    # Assign onmouseover and onmouseout callbacks to patches.
    mypatch = xmlid[f'mypatch_{index:03d}']
    mypatch.set('onmouseover', "ShowTooltip(this)")
    mypatch.set('onmouseout', "HideTooltip(this)")

# This is the script defining the ShowTooltip and HideTooltip functions.
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

# Insert the script at the top of the file and save it.
tree.insert(0, ET.XML(script))
ET.ElementTree(tree).write('svg_tooltip.svg')
```

## Summary

In this lab, we learned how to create a tooltip that will show up when hovering over a matplotlib patch. We created the tooltip in matplotlib and simply toggled its visibility on when hovering over the patch. We also added interactivity to the plot by creating a tooltip that will be toggled on and off when hovering over the patches.
