# Agregar interactividad

Agregamos interactividad a la gráfica creando un mensaje emergente que se activará y desactivará al pasar el cursor sobre los recuadros. Hacemos esto creando un árbol XML a partir del archivo SVG, escondiendo los mensajes emergentes y asignando devoluciones de llamada `onmouseover` y `onmouseout` a los recuadros. También definimos las funciones `ShowTooltip` y `HideTooltip` que se llamarán al pasar el cursor sobre los recuadros.

```python
tree, xmlid = ET.XMLID(f.getvalue())
tree.set('onload', 'init(event)')

for i in shapes:
    # Obtener el índice de la forma
    index = shapes.index(i)
    # Ocultar los mensajes emergentes
    tooltip = xmlid[f'mytooltip_{index:03d}']
    tooltip.set('visibility', 'hidden')
    # Asignar devoluciones de llamada onmouseover y onmouseout a los recuadros.
    mypatch = xmlid[f'mypatch_{index:03d}']
    mypatch.set('onmouseover', "ShowTooltip(this)")
    mypatch.set('onmouseout', "HideTooltip(this)")

# Este es el script que define las funciones ShowTooltip y HideTooltip.
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

# Insertar el script al principio del archivo y guardarlo.
tree.insert(0, ET.XML(script))
ET.ElementTree(tree).write('svg_tooltip.svg')
```
