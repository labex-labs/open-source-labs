# Schriftart für den Titel festlegen

Wir können auch die Schriftfamilie für den Titel mit dem Parameter `math_fontfamily` ändern.

```python
ax.set_title(r"$Title\ in\ math\ mode:\ \int_{0}^{\infty } x^2 dx$",
             math_fontfamily='stixsans', size=14)
```
