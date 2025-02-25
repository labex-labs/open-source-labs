# Rebanado

Rebanar significa tomar una subsecuencia de una secuencia. La sintaxis es `s[start:end]`. Donde `start` y `end` son los índices de la subsecuencia que desees.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

- Los índices `start` y `end` deben ser enteros.
- Las rebanadas _no_ incluyen el valor final. Es como un intervalo semiabierto de matemáticas.
- Si se omiten los índices, por defecto se toman el principio o el final de la lista.
