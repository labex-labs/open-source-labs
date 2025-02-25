# Pivotamiento con agregaciones simples

Pivot es uno de los métodos clave para la remodelación de datos en Pandas. Proporciona una forma de transformar tus datos para que puedas visualizarlos desde diferentes ángulos.

```python
# Pivot df con la media de val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
