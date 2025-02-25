# Transparenz hinzufügen

Der einfachste Weg, Transparenz bei der Darstellung von Daten mit `imshow` zu verwenden, ist es, ein Array mit der gleichen Form wie die Daten an das Argument `alpha` zu übergeben.

```python
# Erstelle einen Alphakanal mit linear zunehmenden Werten, die nach rechts gehen.
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# Erstelle die Figur und das Bild
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
