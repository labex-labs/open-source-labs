# Pasaje de argumentos

Cuando se llama a una función, las variables de argumento son nombres que se refieren a los valores pasados. Estos valores NO son copias. Si se pasan tipos de datos mutables (por ejemplo, listas, diccionarios), se pueden modificar _in situ_.

```python
def foo(items):
    items.append(42)    # Modifica el objeto de entrada

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Punto clave: Las funciones no reciben una copia de los argumentos de entrada.**
