# Steuere das Bild-Origin

```python
# Bestimme, ob Bilder mit dem Array-Origin x[0, 0] in der oberen linken oder unteren rechten Ecke geplottet werden sollen
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('blau sollte oben sein')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('blau sollte unten sein')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```
