# Quadratische geteilte Achsen

Wir werden ein quadratisches Achsenbild mit einer geteilten Achse erzeugen. Die geteilte Achse übernimmt das Seitenverhältnis der übergeordneten Achse.

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```
