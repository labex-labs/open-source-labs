# Encontrar el valor máximo de una lista basado en una función

## Problema

Escribe una función `max_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe mapear cada elemento en `lst` a un valor usando la función `fn` proporcionada y luego devolver el valor máximo.

## Ejemplo

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```

## Restricciones

- La lista `lst` contendrá al menos un elemento.
- La función `fn` tomará un argumento y devolverá un valor.
