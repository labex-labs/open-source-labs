# Variables globales

Las funciones pueden acceder libremente a los valores de las variables globales definidas en el mismo archivo.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Usando la variable global `name`
```

Sin embargo, las funciones no pueden modificar las variables globales:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # imprime 'Dave'
```

**Recuerde: Todas las asignaciones en funciones son locales.**
