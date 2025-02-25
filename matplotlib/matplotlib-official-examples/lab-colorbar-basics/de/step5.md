# Erstellen eines Plots mit positiven und negativen Daten

Wir erstellen einen Plot mit sowohl positiven als auch negativen Daten und fügen mithilfe der `colorbar`-Funktion eine Farbskala zum Plot hinzu. Diesmal legen wir die Mindest- und Maximalwerte für die Farbskala mit den Parametern `vmin` und `vmax` fest.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
