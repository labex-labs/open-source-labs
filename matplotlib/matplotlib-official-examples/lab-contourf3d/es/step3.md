# Generar los datos

Ahora generaremos los datos que se utilizarán en el gráfico de contorno 3D. Utilizaremos el método `axes3d.get_test_data()` para generar los datos. Este método genera datos de prueba para un gráfico tridimensional.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
