# Usando el módulo `inspect`

En Python, la biblioteca estándar incluye un módulo `inspect` muy útil. Este módulo es como una herramienta detective que nos ayuda a recopilar información sobre objetos en tiempo de ejecución (live objects) en Python. Los objetos en tiempo de ejecución pueden ser cosas como módulos, clases y funciones. En lugar de buscar manualmente a través de los atributos de un objeto para encontrar información, el módulo `inspect` proporciona formas más organizadas y de alto nivel de entender las propiedades de las funciones.

Sigamos usando la misma shell interactiva de Python para explorar cómo funciona este módulo.

## Firmas de funciones

La función `inspect.signature()` es una herramienta muy útil. Cuando le pasas una función, devuelve un objeto `Signature`. Este objeto contiene detalles importantes sobre los parámetros de la función.

Aquí tienes un ejemplo. Supongamos que tenemos una función llamada `add`. Podemos usar la función `inspect.signature()` para obtener su firma:

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

Cuando ejecutes este código, la salida será:

```
(x, y)
```

Esta salida nos muestra la firma de la función, que nos dice qué parámetros puede aceptar la función.

## Examinando detalles de los parámetros

Podemos ir un paso más allá y obtener información más detallada sobre cada parámetro de la función.

```python
print(sig.parameters)
```

La salida de este código será:

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

Los parámetros de la función se almacenan en un diccionario ordenado. A veces, solo podríamos estar interesados en los nombres de los parámetros. Podemos convertir este diccionario ordenado en una tupla para extraer solo los nombres de los parámetros.

```python
param_names = tuple(sig.parameters)
print(param_names)
```

La salida será:

```
('x', 'y')
```

## Examinando parámetros individuales

También podemos echar un vistazo más detallado a cada parámetro individual. El siguiente código recorre cada parámetro de la función e imprime algunos detalles importantes sobre él.

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

Este código nos mostrará detalles sobre cada parámetro. Nos dice el tipo de parámetro (si es un parámetro posicional, un parámetro de palabra clave, etc.) y su valor predeterminado si tiene uno.

El módulo `inspect` tiene muchas otras funciones útiles para la introspección de funciones. Aquí tienes algunos ejemplos:

- `inspect.getdoc(obj)`: Esta función recupera la cadena de documentación de un objeto. Las cadenas de documentación son como notas que los programadores escriben para explicar lo que hace un objeto.
- `inspect.getfile(obj)`: Nos ayuda a averiguar el archivo donde está definido un objeto. Esto puede ser muy útil cuando queremos localizar el código fuente de un objeto.
- `inspect.getsource(obj)`: Esta función obtiene el código fuente de un objeto. Nos permite ver exactamente cómo está implementado el objeto.
