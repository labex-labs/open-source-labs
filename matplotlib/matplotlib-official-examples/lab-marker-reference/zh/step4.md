# 由 TeX 符号创建的标记

使用 :ref:`MathText <mathtext>` 来使用自定义标记符号，例如 `"$\u266B$"`。有关 STIX 字体符号的概述，请参阅 `STIX字体表 <http://www.stixfonts.org/allGlyphs.html>`\_。另请参阅 :doc:`/gallery/text_labels_and_annotations/stix_fonts_demo`。

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
