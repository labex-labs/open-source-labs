# Text mit korrekter Rotation plotten

Schließlich werden wir Text an den angegebenen Positionen plotten, wobei die Rotation der Linie berücksichtigt wird. Dies wird dazu führen, dass der Text im richtigen Winkel relativ zur Linie rotiert.

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
