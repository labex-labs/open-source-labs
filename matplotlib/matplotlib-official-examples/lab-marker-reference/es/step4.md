# Marcadores creados a partir de símbolos de TeX

Utilice :ref:`MathText <mathtext>` para utilizar símbolos de marcador personalizados, como `"$\u266B$"`. Para obtener una panorámica de los símbolos de la fuente STIX, consulte la `tabla de fuentes STIX <http://www.stixfonts.org/allGlyphs.html>`\_. También consulte el :doc:`/gallery/text_labels_and_annotations/stix_fonts_demo`.

```python
fig, ax = plt.subplots()
fig.suptitle('Mathtext markers', fontsize=14)
fig.subplots_adjust(left=0.4)

marker_style.update(markeredgecolor="none", markersize=15)
markers = ["$1$", r"$\frac{1}{2}$", "$f$", "$\u266B$", r"$\mathcal{A}$"]

for y, marker in enumerate(markers):
    # Escape dollars so that the text is written "as is", not as mathtext.
    ax.text(-0.5, y, repr(marker).replace("$", r"\$"), **text_style)
    ax.plot([y] * 3, marker=marker, **marker_style)
format_axes(ax)
```
