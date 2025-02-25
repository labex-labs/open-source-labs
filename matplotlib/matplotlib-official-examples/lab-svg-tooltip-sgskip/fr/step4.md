# Ajouter de l'interactivité

Nous ajoutons de l'interactivité à la figure en créant un tool-tip qui sera activé et désactivé lorsqu'on survole les patches. Nous le faisons en créant un arbre XML à partir du fichier SVG, en cachant les tool-tips et en assignant des rappels `onmouseover` et `onmouseout` aux patches. Nous définissons également les fonctions `ShowTooltip` et `HideTooltip` qui seront appelées lorsqu'on survole les patches.

```python
tree, xmlid = ET.XMLID(f.getvalue())
tree.set('onload', 'init(event)')

for i in shapes:
    # Obtenez l'index de la forme
    index = shapes.index(i)
    # Cachez les tool-tips
    tooltip = xmlid[f'mytooltip_{index:03d}']
    tooltip.set('visibility', 'hidden')
    # Assignez des rappels onmouseover et onmouseout aux patches.
    mypatch = xmlid[f'mypatch_{index:03d}']
    mypatch.set('onmouseover', "ShowTooltip(this)")
    mypatch.set('onmouseout', "HideTooltip(this)")

# Voici le script définissant les fonctions ShowTooltip et HideTooltip.
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

# Insérez le script en haut du fichier et enregistrez-le.
tree.insert(0, ET.XML(script))
ET.ElementTree(tree).write('svg_tooltip.svg')
```
