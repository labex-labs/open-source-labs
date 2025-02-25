# Establecer la regla de recurrencia

Se van a establecer marcas de fecha personalizadas en cada quinto domingo de Pascua. Para hacer esto, es necesario establecer la regla de recurrencia utilizando la función `rrulewrapper`.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```
