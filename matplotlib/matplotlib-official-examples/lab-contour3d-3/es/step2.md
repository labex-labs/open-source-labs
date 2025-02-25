# Crear una figura 3D y datos

En este paso, crearemos una figura 3D y obtendremos datos de prueba para la representación gráfica de la superficie.

```python
# Crea una figura 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Obtiene datos de prueba para la representación gráfica de la superficie
X, Y, Z = axes3d.get_test_data(0.05)
```
