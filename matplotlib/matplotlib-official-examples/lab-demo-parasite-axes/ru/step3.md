# Создаем паразитные оси

Мы создаем две паразитные оси с помощью метода `host.get_aux_axes()`. Мы устанавливаем `viewlim_mode=None`, чтобы гарантировать, что паразитные оси имеют ту же шкалу по оси x, что и основная ось. Мы также устанавливаем `sharex=host`, чтобы обеспечить совместное использование шкалы по оси x.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
