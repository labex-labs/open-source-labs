# Crear etiquetas de fila

Crearemos etiquetas de fila para el conjunto de datos para representar el número de años para los cuales se han registrado las pérdidas. Usaremos una comprensión de lista para crear las etiquetas de fila.

```python
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
```
