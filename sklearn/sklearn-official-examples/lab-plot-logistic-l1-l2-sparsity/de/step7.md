# Visualisierung der Koeffizienten

Wir werden die Koeffizienten der Modelle für jede Strafe und jeden `C`-Wert visualisieren.

```python
    for ax, coefs in zip(axes_row, [coef_l1_LR, coef_en_LR, coef_l2_LR]):
        ax.imshow(np.abs(coefs.reshape(8, 8)), interpolation='nearest', cmap='binary', vmax=1, vmin=0)
        ax.set_xticks(())
        ax.set_yticks(())
```
