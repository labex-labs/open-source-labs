# Cadena de texto a palabras

Escribe una función `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` que tome una cadena de texto `s` y una cadena `pattern` opcional como argumentos y devuelva una lista de palabras de la cadena de texto.

- La función debe utilizar `re.findall()` con el `pattern` suministrado para encontrar todas las subcadenas coincidentes.
- Si no se proporciona el argumento `pattern`, la función debe utilizar la expresión regular predeterminada, que coincide con caracteres alfanuméricos y guiones.

```python
import re

def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
```

```python
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b')
# ['build', 'q', 'out', 'one-item']
```
