# Manejo de patrones más complejos

Nuestra función actual funciona para camelCase, pero necesitamos mejorarla para manejar patrones adicionales como:

1. PascalCase (por ejemplo, `HelloWorld`)
2. Cadenas con guiones (por ejemplo, `hello-world`)
3. Cadenas que ya tienen guiones bajos (por ejemplo, `hello_world`)

Actualicemos nuestra función para manejar estos casos:

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

Las mejoras que hicimos:

1. Primero, reemplazamos cualquier guión con un espacio.
2. La nueva expresión regular `re.sub('([A-Z]+)', r' \1', s)` agrega un espacio antes de cualquier secuencia de letras mayúsculas, lo que ayuda con PascalCase.
3. Mantenemos nuestra expresión regular para manejar camelCase.
4. Finalmente, dividimos la cadena por espacios, la unimos con guiones bajos y la convertimos a minúsculas, lo que maneja cualquier espacio restante y asegura una salida consistente.

Ejecuta tu script para probar con varios formatos de entrada:

```bash
python3 ~/project/snake_case.py
```

Deberías ver una salida como esta:

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

Nuestra función ahora es más robusta y puede manejar varios formatos de entrada. En el siguiente paso, haremos nuestros refinamientos finales y la probaremos con la suite de pruebas completa.
