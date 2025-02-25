# Cargar datos

Cargaremos una matriz de registros de numpy a partir de datos csv de yahoo con los campos fecha, apertura, alta, baja, cierre, volumen, cierre ajustado del directorio mpl-data/sample_data. La matriz de registros almacena la fecha como un np.datetime64 con una unidad de día ('D') en la columna de fecha.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # obtener los últimos 250 días de trading
```
