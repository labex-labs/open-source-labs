# Creación de la función básica

Comencemos por crear el núcleo de nuestra función. La construiremos paso a paso. Primero, crea un archivo llamado `key_of_max.py`. Puedes utilizar el editor de código incorporado de LabEx, o un editor basado en terminal como `nano` o `vim`. Dentro de `key_of_max.py`, agrega el siguiente código:

![Code editor with key_of_max function](../assets/20250214-14-44-53-838b9T58.png)

```python
def key_of_max(d):
  """
  Devuelve la clave asociada con el valor máximo en el diccionario 'd'.

  Si múltiples claves comparten el valor máximo, cualquiera de ellas puede ser devuelta.
  """
  return max(d, key=d.get)
```

A continuación, una desglose:

- **`def key_of_max(d):`**: Esto define una función llamada `key_of_max`. Toma un argumento, `d`, que representa el diccionario con el que trabajaremos.
- **`return max(d, key=d.get)`**: Este es el corazón de la función. Analicémoslo parte por parte:
  - **`max(d,...)`**: La función incorporada `max()` encuentra el elemento más grande. Por defecto, si le das a `max()` un diccionario, encontrará la clave más grande (alfabéticamente). No queremos eso; queremos la clave asociada con el valor más grande.
  - **`key=d.get`**: Esta es la parte crucial. El argumento `key` le dice a `max()` cómo comparar los elementos. `d.get` es un método de los diccionarios. Cuando llamas a `d.get(alguna_clave)`, devuelve el valor asociado con `alguna_clave`. Al establecer `key=d.get`, le estamos diciendo a `max()`: "Compara los elementos en el diccionario `d` utilizando sus valores, no sus claves". La función `max()` luego devuelve la clave correspondiente a ese valor máximo.
