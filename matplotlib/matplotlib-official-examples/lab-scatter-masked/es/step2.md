# Generando datos para el diagrama de dispersión

A continuación, generamos datos para el diagrama de dispersión. Creamos 100 puntos de datos con valores aleatorios de x e y entre 0 y 0,9, y radios aleatorios entre 0 y 10. El color de cada punto de datos está determinado por la raíz cuadrada de su área.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
```
