# TeX 심볼 (TeX Symbols) 로 생성된 마커

:ref:`MathText <mathtext>`를 사용하여, 예를 들어 `"$\u266B$"`와 같은 사용자 정의 마커 심볼을 사용할 수 있습니다. STIX 폰트 심볼에 대한 개요는 `STIX 폰트 테이블 <http://www.stixfonts.org/allGlyphs.html>`\_을 참조하십시오. 또한 :doc:`/gallery/text_labels_and_annotations/stix_fonts_demo`도 참조하십시오.

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
