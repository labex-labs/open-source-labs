# Einige Dreiecke maskieren

Wir maskieren einige der Dreiecke im Gitter, um ungültige Daten zu simulieren. Wir wählen zufällig einen Teilmengen von Dreiecken basierend auf dem Parameter `init_mask_frac` aus.

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
