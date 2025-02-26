# Espacios de nombres

Un módulo es una colección de valores con nombre y a veces se dice que es un _espacio de nombres_. Los nombres son todas las variables y funciones globales definidas en el archivo fuente. Después de importar, el nombre del módulo se utiliza como prefijo. De ahí el _espacio de nombres_.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

El nombre del módulo está directamente ligado al nombre del archivo (foo -> foo.py).
