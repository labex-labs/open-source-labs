# Cargar datos

A continuación, cargaremos los datos que queremos representar. Utilizaremos una matriz de registros de numpy a partir de datos csv de Yahoo con los campos fecha, apertura, alta, baja, cierre, volumen, cierre ajustado del directorio mpl-data/sample_data. La matriz de registros almacena la fecha como un np.datetime64 con una unidad de día ('D') en la columna de fecha.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
