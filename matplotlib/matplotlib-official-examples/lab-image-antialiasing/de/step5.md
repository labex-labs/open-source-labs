# Bild mit 'antialiased' Interpolation aufvergrößern

Schließlich werden wir das Bild von 500 Datenpunkten auf 530 gerenderte Pixel mit 'antialiased' Interpolation aufvergrößern. Dies wird demonstrieren, wie die Verwendung besserer Entzerrungsalgorithmen die Moiré-Muster reduzieren kann.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
