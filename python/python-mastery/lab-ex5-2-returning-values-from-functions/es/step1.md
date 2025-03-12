# Devolviendo múltiples valores desde funciones

En Python, cuando necesitas que una función devuelva más de un valor, hay una solución práctica: devolver una tupla. Una tupla es un tipo de estructura de datos en Python. Es una secuencia inmutable, lo que significa que una vez que creas una tupla, no puedes cambiar sus elementos. Las tuplas son útiles porque pueden contener múltiples valores de diferentes tipos en un solo lugar.

Vamos a crear una función para analizar líneas de configuración en el formato `nombre=valor`. El objetivo de esta función es tomar una línea en este formato y devolver tanto el nombre como el valor como elementos separados.

1. Primero, necesitas crear un nuevo archivo de Python. Este archivo contendrá el código de nuestra función y el código de prueba. En el directorio del proyecto, crea un archivo llamado `return_values.py`. Puedes usar el siguiente comando en la terminal para crear este archivo:

```
touch ~/project/return_values.py
```

2. Ahora, abre el archivo `return_values.py` en tu editor de código. Dentro de este archivo, escribiremos la función `parse_line`. Esta función toma una línea como entrada, la divide en el primer signo '=' y devuelve el nombre y el valor como una tupla.

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

En esta función, el método `split` se utiliza para dividir la línea de entrada en dos partes en el primer signo '='. Si la línea está en el formato correcto `nombre=valor`, extraemos el nombre y el valor y los devolvemos como una tupla.

3. Después de definir la función, necesitamos agregar algún código de prueba para ver si la función funciona como se espera. El código de prueba llamará a la función `parse_line` con una entrada de muestra e imprimirá los resultados.

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

En el código de prueba, primero llamamos a la función `parse_line` y almacenamos la tupla devuelta en la variable `result`. Luego imprimimos esta tupla. A continuación, usamos el desempaquetado de tuplas para asignar directamente los elementos de la tupla a las variables `name` y `value` e imprimirlos por separado.

4. Una vez que hayas escrito la función y el código de prueba, guarda el archivo `return_values.py`. Luego, abre la terminal y ejecuta el siguiente comando para ejecutar el script de Python:

```
python ~/project/return_values.py
```

Deberías ver una salida similar a:

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**Explicación:**

- La función `parse_line` divide la cadena de entrada en el carácter '=' utilizando el método `split`. Este método divide la cadena en partes basadas en el separador especificado.
- Devuelve ambas partes como una tupla utilizando la sintaxis `return (name, value)`. Una tupla es una forma de agrupar múltiples valores juntos.
- Cuando se llama a la función, tienes dos opciones. Puedes almacenar la tupla completa en una variable, como hicimos con la variable `result`. O puedes "desempaquetar" la tupla directamente en variables separadas utilizando la sintaxis `name, value = parse_line(...)`. Esto facilita trabajar con los valores individuales.

Este patrón de devolver múltiples valores como una tupla es muy común en Python. Hace que las funciones sean más versátiles porque pueden proporcionar más de una pieza de información al código que las llama.
