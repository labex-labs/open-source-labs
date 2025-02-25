# Encontrar el nombre más largo

Vamos a averiguar cuál pasajero del Titanic tiene el nombre más largo. Utilizaremos el método `str.len()` para obtener la longitud de cada nombre y el método `idxmax()` para encontrar el índice del nombre más largo.

```python
# Obtener la longitud de cada nombre
longitudes_nombres = titanic["Nombre"].str.len()

# Encontrar el índice del nombre más largo
índice_nombre_más_largo = longitudes_nombres.idxmax()

# Obtener el nombre más largo
nombre_más_largo = titanic.loc[índice_nombre_más_largo, "Nombre"]
```
