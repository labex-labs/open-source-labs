# Erstelle Parasitenachsen

Wir erstellen zwei Parasitenachsen mit der `host.get_aux_axes()`-Methode. Wir setzen `viewlim_mode=None`, um sicherzustellen, dass die Parasitenachsen die gleiche x-Skala mit der Hauptachse teilen. Wir setzen auch `sharex=host`, um sicherzustellen, dass die x-Skala geteilt wird.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
