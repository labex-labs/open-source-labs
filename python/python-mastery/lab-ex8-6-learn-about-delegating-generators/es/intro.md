# Introducción

**Objetivos:**

- Aprender sobre la delegación de generadores

**Archivos modificados:** `cofollow.py`, `server.py`

Un problema potencial en el código que depende de generadores es el de ocultar detalles al usuario y al escribir bibliotecas. Generalmente se requieren muchos mecanismos de bajo nivel para controlar todo y a menudo es bastante incómodo exponerlos directamente a los usuarios.

A partir de Python 3.3, se puede utilizar una nueva declaración `yield from` para delegar generadores a otra función. Es una forma útil de limpiar el código que depende de generadores.
