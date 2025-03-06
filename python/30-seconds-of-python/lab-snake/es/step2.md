# Uso de expresiones regulares para la coincidencia de patrones

Para convertir cadenas a snake case, utilizaremos expresiones regulares (regex) para identificar los límites de las palabras. El módulo `re` en Python proporciona poderosas capacidades de coincidencia de patrones que podemos utilizar para esta tarea.

Actualicemos nuestra función para manejar cadenas en camelCase:

1. Primero, necesitamos identificar el patrón en el que una letra minúscula va seguida de una letra mayúscula (como en "camelCase").
2. Luego, insertaremos un espacio entre ellas.
3. Finalmente, convertiremos todo a minúsculas y reemplazaremos los espacios por guiones bajos.

Actualiza tu archivo `snake_case.py` con esta función mejorada:

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Desglosemos lo que hace esta función:

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` busca patrones en los que una letra minúscula `([a-z])` va seguida de una letra mayúscula `([A-Z])`. Luego, reemplaza este patrón con las mismas letras pero agrega un espacio entre ellas utilizando `\1` y `\2`, que se refieren a los grupos capturados.
- Luego convertimos todo a minúsculas con `lower()` y reemplazamos los espacios por guiones bajos.

Ejecuta tu script nuevamente para ver si funciona con cadenas en camelCase:

```bash
python3 ~/project/snake_case.py
```

La salida ahora debería ser:

```
Original: helloWorld
Snake case: hello_world
```

¡Genial! Nuestra función ahora puede manejar cadenas en camelCase. En el siguiente paso, la mejoraremos para manejar casos más complejos.
