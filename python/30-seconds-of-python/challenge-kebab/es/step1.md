# Cadena en formato kebab case

## Problema

Escribe una función de Python llamada `to_kebab_case(s)` que tome una cadena `s` como entrada y devuelva la versión de la cadena en formato kebab case. La función debe realizar los siguientes pasos:

1. Reemplaza cualquier `-` o `_` con un espacio, utilizando la expresión regular `r"(_|-)+"`.
2. Encuentra todas las palabras en la cadena y las convierte a minúsculas con `str.lower()`.
3. Combina todas las palabras utilizando `-` como separador.

## Ejemplo

```python
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```
