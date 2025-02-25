# Créez des axes parasites

Nous créons deux axes parasites en utilisant la méthode `host.get_aux_axes()`. Nous définissons `viewlim_mode=None` pour vous assurer que les axes parasites partagent la même échelle x que les axes hôtes. Nous définissons également `sharex=host` pour vous assurer que l'échelle x est partagée.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
