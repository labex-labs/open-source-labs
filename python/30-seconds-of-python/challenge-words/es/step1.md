# Desafío de convertir una cadena en palabras

## Problema

Escribe una función `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` que tome una cadena `s` y una cadena `pattern` opcional como argumentos y devuelva una lista de palabras en la cadena.

- La función debe utilizar `re.findall()` con el `pattern` suministrado para encontrar todas las subcadenas coincidentes.
- Si no se proporciona el argumento `pattern`, la función debe utilizar la expresión regular predeterminada, que coincide con caracteres alfanuméricos y guiones.

## Ejemplo

```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```
