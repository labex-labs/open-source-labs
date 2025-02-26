# Devolviendo múltiples valores

Supongamos que estuvieras escribiendo código para analizar archivos de configuración que consisten en líneas como esta:

    nombre=valor

Escribe una función `parse_line(line)` que tome una línea de este tipo y devuelva tanto el nombre asociado como el valor. La convención común para devolver múltiples valores es devolverlos en una tupla. Por ejemplo:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> nombre, val = parse_line('email=guido@python.org')
>>> nombre
'email'
>>> val
'guido@python.org'
>>>
```
