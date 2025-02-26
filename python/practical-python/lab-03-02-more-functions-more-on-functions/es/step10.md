# Modificando variables globales

Si es necesario modificar una variable global, debe declararse como tal.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Cambia la variable global name arriba
```

La declaración global debe aparecer antes de su uso y la variable correspondiente debe existir en el mismo archivo que la función. Habiendo visto esto, sabe que se considera mala forma. De hecho, trate de evitar `global` por completo si puede. Si necesita que una función modifique algún tipo de estado fuera de la función, es mejor usar una clase en su lugar (más sobre esto más adelante).
