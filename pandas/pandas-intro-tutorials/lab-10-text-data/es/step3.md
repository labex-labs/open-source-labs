# Extraer los apellidos de los nombres completos

Ahora, creemos una nueva columna `Apellido` que contenga el apellido de los pasajeros. Lo haremos extrayendo la parte antes de la coma en la columna `Nombre`.

```python
# Dividir la columna 'Nombre' por coma y extraer la primera parte
titanic["Apellido"] = titanic["Nombre"].str.split(",").str.get(0)
```
