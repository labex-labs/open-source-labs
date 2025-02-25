# Crear ejes parasitos

Creamos dos ejes parasitos utilizando el método `host.get_aux_axes()`. Establecemos `viewlim_mode=None` para garantizar que los ejes parasitos compartan la misma escala en x con el eje principal. También establecemos `sharex=host` para asegurar que se comparta la escala en x.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
