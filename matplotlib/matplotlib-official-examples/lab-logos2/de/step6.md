# Anzeigen der Logos

In diesem Schritt werden wir die Matplotlib-Logos in verschiedenen Größen anzeigen.

```python
# Ein großes Logo:
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# Ein kleines 32px-Logo:
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# Ein großes Logo mit Text, wie es auf der Matplotlib-Website verwendet wird.
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
