# Comprendiendo el problema

Antes de escribir nuestra función de conversión a snake case, entendamos lo que necesitamos lograr:

1. Necesitamos convertir una cadena de cualquier formato a snake case.
2. Snake case significa que todas las letras son minúsculas y hay guiones bajos entre las palabras.
3. Necesitamos manejar diferentes formatos de entrada:
   - camelCase (por ejemplo, `camelCase` → `camel_case`)
   - Cadenas con espacios (por ejemplo, `some text` → `some_text`)
   - Cadenas con formato mixto (por ejemplo, guiones, guiones bajos y mayúsculas y minúsculas mezcladas)

Comencemos creando un nuevo archivo de Python para nuestra función de snake case. En el WebIDE, navega al directorio del proyecto y crea un nuevo archivo llamado `snake_case.py`:

```python
# This function will convert a string to snake case
def snake(s):
    # We'll implement this function step by step
    pass  # Placeholder for now

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Guarda este archivo. En el siguiente paso, comenzaremos a implementar la función.

Por ahora, ejecutemos nuestra función de marcador de posición para asegurarnos de que nuestro archivo esté configurado correctamente. Abre una terminal y ejecuta:

```bash
python3 ~/project/snake_case.py
```

![python-prompt](../assets/screenshot-20250306-B5lI9tyo@2x.png)

Deberías ver una salida como esta:

```
Original: helloWorld
Snake case: None
```

El resultado es `None` porque nuestra función actualmente solo devuelve el valor predeterminado de Python `None`. En el siguiente paso, agregaremos la lógica real de conversión.
