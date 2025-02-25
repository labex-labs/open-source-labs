# Text ohne korrekte Rotation plotten

Wir werden nun Text an den angegebenen Positionen plotten, ohne die Rotation der Linie zu berücksichtigen. Dies wird dazu führen, dass der Text im 45-Grad-Winkel rotiert wird, was nicht das gewünschte Ergebnis ist.

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
