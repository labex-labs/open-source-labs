# Marcadores Criados a partir de Símbolos TeX

Use :ref:`MathText <mathtext>` para usar símbolos de marcador personalizados, como por exemplo, `"$\u266B$"`. Para uma visão geral dos símbolos da fonte STIX, consulte a `tabela de fontes STIX <http://www.stixfonts.org/allGlyphs.html>`\_. Veja também o :doc:`/gallery/text_labels_and_annotations/stix_fonts_demo`.

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
