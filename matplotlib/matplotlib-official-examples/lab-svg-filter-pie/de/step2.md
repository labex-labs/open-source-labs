# Speichern des Diagramms als SVG

Wir werden das Kreisdiagramm als SVG-Datei speichern, indem wir die Module io und xml.etree.ElementTree verwenden. Wir werden die Filterdefinition für den Schatten mit einem Gaußschen Blur und einem Beleuchtungseffekt definieren. Der Beleuchtungsfilter wird von http://www.w3.org/TR/SVG/filters.html kopiert. Wir werden den Filter mit Inkscape und Firefox3 testen, beachten Sie jedoch, dass die Exportfunktion von Inkscape möglicherweise nicht unterstützt.

```python
import io
import xml.etree.ElementTree as ET

f = io.BytesIO()
plt.savefig(f, format="svg")

filter_def = """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='2'/>
    </filter>

    <filter id='MyFilter' filterUnits='objectBoundingBox'
            x='0' y='0' width='1' height='1'>
      <feGaussianBlur in='SourceAlpha' stdDeviation='4%' result='blur'/>
      <feOffset in='blur' dx='4%' dy='4%' result='offsetBlur'/>
      <feSpecularLighting in='blur' surfaceScale='5' specularConstant='.75'
           specularExponent='20' lighting-color='#bbbbbb' result='specOut'>
        <fePointLight x='-5000%' y='-10000%' z='20000%'/>
      </feSpecularLighting>
      <feComposite in='specOut' in2='SourceAlpha'
                   operator='in' result='specOut'/>
      <feComposite in='SourceGraphic' in2='specOut' operator='arithmetic'
    k1='0' k2='1' k3='1' k4='0'/>
    </filter>
  </defs>
"""

tree, xmlid = ET.XMLID(f.getvalue())
tree.insert(0, ET.XML(filter_def))

for i, pie_name in enumerate(labels):
    pie = xmlid[pie_name]
    pie.set("filter", 'url(#MyFilter)')

    shadow = xmlid[pie_name + "_shadow"]
    shadow.set("filter", 'url(#dropshadow)')

fn = "svg_filter_pie.svg"
print(f"Saving '{fn}'")
ET.ElementTree(tree).write(fn)
```
