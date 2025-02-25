# Crear la malla

A continuación, crearemos la malla en coordenadas polares y calcularemos el Z correspondiente. Crearemos una matriz de valores de radio `r`, una matriz de valores de ángulo `p`, y luego usaremos la función `meshgrid()` de NumPy para crear una cuadrícula de valores de `R` y `P`. Finalmente, usaremos la ecuación de `Z` para calcular la altura de cada punto en la superficie.

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```
