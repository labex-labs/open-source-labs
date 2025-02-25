# Zeige das MRI-Bild an

Wir werden die `imshow`-Funktion aus `matplotlib` verwenden, um das MRI-Bild in Graustufen anzuzeigen.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
