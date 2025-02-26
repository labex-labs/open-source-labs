# Programas principales vs. importaciones de bibliotecas

Cualquier archivo de Python puede ejecutarse como principal o como una importación de biblioteca:

```bash
$ python3 prog.py # Ejecutándose como principal
```

```python
import prog   # Ejecutándose como importación de biblioteca
```

En ambos casos, `__name__` es el nombre del módulo. Sin embargo, solo se establecerá en `__main__` si se ejecuta como principal.

Por lo general, no se desea que las declaraciones que forman parte del programa principal se ejecuten durante una importación de biblioteca. Por lo tanto, es común tener una comprobación `if` en el código que puede usarse de cualquiera de las dos maneras.

```python
if __name__ == '__main__':
    # No se ejecuta si se carga con import...
```
