# Verificación de `__main__`

Es una práctica estándar para los módulos que se ejecutan como un script principal utilizar esta convención:

```python
# prog.py
...
if __name__ == '__main__':
    # Ejecutándose como el programa principal...
    declaraciones
  ...
```

Las declaraciones incluidas dentro de la instrucción `if` se convierten en el _programa principal_.
