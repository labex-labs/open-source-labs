# Métodos de cadenas

Las cadenas tienen métodos que realizan diversas operaciones con los datos de la cadena.

Ejemplo: eliminar cualquier espacio en blanco al principio / al final.

```python
s ='  Hello '
t = s.strip()     # 'Hello'
```

Ejemplo: conversión de mayúsculas y minúsculas.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Ejemplo: reemplazar texto.

```python
s = 'Hello world'
t = s.replace('Hello', 'Hallo')   # 'Hallo world'
```

**Más métodos de cadenas:**

Las cadenas tienen una amplia variedad de otros métodos para probar y manipular los datos de texto. Este es un pequeño ejemplo de métodos:

```python
s.endswith(suffix)     # Comprobar si la cadena termina con el sufijo
s.find(t)              # Primera aparición de t en s
s.index(t)             # Primera aparición de t en s
s.isalpha()            # Comprobar si los caracteres son alfabéticos
s.isdigit()            # Comprobar si los caracteres son numéricos
s.islower()            # Comprobar si los caracteres son en minúsculas
s.isupper()            # Comprobar si los caracteres son en mayúsculas
s.join(slist)          # Unir una lista de cadenas usando s como delimitador
s.lower()              # Convertir a minúsculas
s.replace(old,new)     # Reemplazar texto
s.rfind(t)             # Buscar t desde el final de la cadena
s.rindex(t)            # Buscar t desde el final de la cadena
s.split([delim])       # Dividir la cadena en una lista de subcadenas
s.startswith(prefix)   # Comprobar si la cadena empieza con el prefijo
s.strip()              # Quitar el espacio en blanco al principio / al final
s.upper()              # Convertir a mayúsculas
```
