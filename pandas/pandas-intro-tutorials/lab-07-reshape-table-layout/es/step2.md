# Ordenar filas de la tabla

Ordene el conjunto de datos del Titanic según la edad de los pasajeros y luego por clase de cabina y edad en orden descendente.

```python
# Ordenar por Edad
titanic.sort_values(by="Age").head()

# Ordenar por Pclass y Edad en orden descendente
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
