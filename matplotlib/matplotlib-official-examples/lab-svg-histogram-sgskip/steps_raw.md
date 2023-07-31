# Creating an Interactive Histogram with Matplotlib

## Introduction

In this lab, we will learn how to create an interactive histogram using Matplotlib. The interactivity is encoded in ECMAScript (JavaScript) and inserted in the SVG code in a post-processing step. The resulting histogram will have bars that can be hidden or shown by clicking on legend markers.

## Steps

### Step 1: Create the Histogram, Legend, and Title

First, we will create the histogram, legend, and title using Matplotlib. We will also assign IDs to each object using the `set_gid()` method. This will help relate Matplotlib objects created in Python and the corresponding SVG constructs that are parsed in the second step.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create histogram, legend, and title
plt.figure()
r = np.random.randn(100)
r1 = r + 1
labels = ['Rabbits', 'Frogs']
H = plt.hist([r, r1], label=labels)
containers = H[-1]
leg = plt.legend(frameon=False)
plt.title("From a web browser, click on the legend\n"
          "marker to toggle the corresponding histogram.")

# Assign IDs to the SVG objects we'll modify
hist_patches = {}
for ic, c in enumerate(containers):
    hist_patches[f'hist_{ic}'] = []
    for il, element in enumerate(c):
        element.set_gid(f'hist_{ic}_patch_{il}')
        hist_patches[f'hist_{ic}'].append(f'hist_{ic}_patch_{il}')

# Set IDs for the legend patches
for i, t in enumerate(leg.get_patches()):
    t.set_gid(f'leg_patch_{i}')

# Set IDs for the text patches
for i, t in enumerate(leg.get_texts()):
    t.set_gid(f'leg_text_{i}')
```

### Step 2: Add Interactivity to the Histogram

Next, we will add interactivity to the histogram by modifying the SVG code using ECMAScript (JavaScript). We will add attributes to the patch and text objects using the `set()` method. We will also create a global variable `container` that stores the patches ID belonging to each histogram. Finally, we will create a function `toggle_hist()` that sets the visibility attribute of all patches of each histogram and the opacity of the marker itself.

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

    a = (a == values[0] || a == "") ? values[1] : values[0];
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

### Step 3: View the Interactive Histogram

Finally, we can view the interactive histogram by opening the SVG file in a web browser. To hide or show the bars, simply click on the legend markers.

### Summary

In this lab, we learned how to create an interactive histogram using Matplotlib. We used ECMAScript (JavaScript) to add interactivity to the histogram by modifying the SVG code. The resulting histogram has bars that can be hidden or shown by clicking on legend markers.
