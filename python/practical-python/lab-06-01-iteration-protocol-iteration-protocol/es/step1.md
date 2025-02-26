# Iteración en todos lados

Muchos objetos diferentes admiten iteración.

```python
a = 'hello'
for c in a: # Recorre los caracteres de a
  ...

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # Recorre las claves en el diccionario
  ...

c = [1,2,3,4]
for i in c: # Recorre los elementos de una lista/tupla
  ...

f = open('foo.txt')
for x in f: # Recorre las líneas de un archivo
  ...
```
