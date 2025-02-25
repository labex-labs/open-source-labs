# Encuentra la clave de un valor en un diccionario

## Problema

Escribe una función `encontrar_clave(dic, val)` que encuentre la primera clave en el diccionario proporcionado que tenga el valor dado.

Tu función debe:

- Tomar un diccionario `dic` y un valor `val` como entrada.
- Utilizar `diccionario.items()` y `next()` para devolver la primera clave que tenga un valor igual a `val`.
- Devolver la clave como salida.

## Ejemplo

```python
edades = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
encontrar_clave(edades, 11) # 'Isabel'
```
