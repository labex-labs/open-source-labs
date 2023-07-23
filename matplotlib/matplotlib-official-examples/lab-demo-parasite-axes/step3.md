# Create parasite axes

We create two parasite axes using `host.get_aux_axes()` method. We set `viewlim_mode=None` to ensure that the parasite axes share the same x-scale with the host axes. We also set `sharex=host` to ensure that the x-scale is shared.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
