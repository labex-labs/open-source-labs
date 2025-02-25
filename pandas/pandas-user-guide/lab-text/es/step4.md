# Probar cadenas

Puedes comprobar si los elementos contienen o coinciden con un patrón utilizando los métodos `contains` y `match` respectivamente.

```python
# comprobar si cada cadena contiene el patrón "a"
s.str.contains("a", na=False)

# comprobar si cada cadena coincide con el patrón "a"
s.str.match("a", na=False)
```
