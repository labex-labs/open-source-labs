# Marqueurs créés à partir de symboles TeX

Utilisez :ref:`MathText <mathtext>` pour utiliser des symboles de marqueurs personnalisés, comme par exemple `"$\u266B$"`. Pour une vue d'ensemble des symboles de police STIX, consultez le `tableau de caractères STIX <http://www.stixfonts.org/allGlyphs.html>`\_. Consultez également le :doc:`/gallery/text_labels_and_annotations/stix_fonts_demo`.

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
