# Cargar datos

A continuación, cargaremos los datos de muestra que utilizaremos en este tutorial. Utilizaremos el archivo `jacksboro_fault_dem.npz`, que contiene datos de elevación.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
