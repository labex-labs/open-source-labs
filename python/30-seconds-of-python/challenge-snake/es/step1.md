# Cadena en formato snake case

## Problema

Escribe una función de Python llamada `snake` que tome una cadena como argumento y devuelva la cadena en formato snake case. La función debe realizar los siguientes pasos:

1. Utiliza `re.sub()` para coincidir con todas las palabras en la cadena y `str.lower()` para convertirlas a minúsculas.
2. Utiliza `re.sub()` para reemplazar cualquier carácter `-` por espacios.
3. Finalmente, utiliza `str.join()` para combinar todas las palabras utilizando `_` como separador.

Tu función debe ser capaz de manejar cadenas con una mezcla de letras mayúsculas y minúsculas, espacios, guiones y subrayados.

## Ejemplo

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
