# Cargar los datos

A continuación, cargamos los datos de elevación de muestra utilizando la función `get_sample_data` de Matplotlib. Luego, extraemos los datos de elevación y el tamaño de celda de la cuadrícula.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
