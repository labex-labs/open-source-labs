# Convertir numpy.datetime64 a fecha de Matplotlib

Los objetos `numpy.datetime64` tienen una precisión de microsegundos para un espacio de tiempo mucho más amplio que los objetos `.datetime`. Sin embargo, actualmente, la hora de Matplotlib solo se convierte de vuelta a objetos datetime, que tienen una resolución de microsegundos y años que solo abarcan desde 0000 hasta 9999.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
