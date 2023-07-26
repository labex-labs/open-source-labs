# Markers Created from TeX Symbols

Use :ref:`MathText <mathtext>`, to use custom marker symbols, like e.g. `"$\u266B$"`. For an overview over the STIX font symbols refer to the `STIX font table <http://www.stixfonts.org/allGlyphs.html>`\_. Also see the :doc:`/gallery/text_labels_and_annotations/stix_fonts_demo`.

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
