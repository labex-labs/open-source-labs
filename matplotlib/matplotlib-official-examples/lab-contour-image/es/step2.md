# Definir los datos

En este paso, definirá los datos que se van a representar. Los datos son una matriz bidimensional de valores que representa la superficie.

```python
# El delta predeterminado es grande porque eso lo hace rápido y demuestra
# el correcto registro entre la imagen y los contornos.
delta = 0.5

extent = (-3, 4, -4, 3)

x = np.arange(-3.0, 4.001, delta)
y = np.arange(-4.0, 3.001, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
