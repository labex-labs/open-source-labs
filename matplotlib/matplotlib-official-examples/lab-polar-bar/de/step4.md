# Erstellen eines Polardiagramms

Wir werden ein Polardiagramm mit dem Parameter `projection='polar'` erstellen.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
