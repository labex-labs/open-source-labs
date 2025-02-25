# Zeige das Bild an

Jetzt können wir das Bild mit der `imshow`-Methode von Matplotlib anzeigen. Wir werden auch die Achsen deaktivieren, sodass wir nur das Bild sehen.

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```
