# Créez le tracé

Maintenant, nous créons un tracé avec deux axes des y à l'aide de la fonction `subplots()` de `matplotlib.pyplot`. Nous connectons également l'événement `ylim_changed` du premier axe à la fonction `convert_ax_c_to_celsius()`.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```
