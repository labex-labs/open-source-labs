# Bild mit 'nearest' Interpolation aufvergrößern

Jetzt werden wir das Bild von 500 Datenpunkten auf 530 gerenderte Pixel mit 'nearest' Interpolation aufvergrößern. Dies wird demonstrieren, dass Moiré-Muster auch bei der Aufvergrößerung des Bildes auftreten können, wenn der Aufvergrößerungsfaktor keine ganze Zahl ist.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```
