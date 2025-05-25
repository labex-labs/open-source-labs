# Criar eixos parasitas

Criamos dois eixos parasitas usando o método `host.get_aux_axes()`. Definimos `viewlim_mode=None` para garantir que os eixos parasitas compartilhem a mesma escala x com os eixos hospedeiros. Também definimos `sharex=host` para garantir que a escala x seja compartilhada.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
