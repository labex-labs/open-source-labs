# Crear datos de muestra

A continuación, crearemos datos de muestra para nuestra gráfica utilizando NumPy. Generaremos 100 puntos de datos entre 0 y 2π y calcularemos sus valores correspondientes de seno.

```python
x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)
```
