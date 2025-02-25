# Configurar los vectores y matrices de la encuesta

A continuación, configura los vectores y matrices de la encuesta. Diseña la carga del disco y la relación de transmisión.

```python
nx = 101
ny = 105

# Configurar vectores de encuesta
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Configurar matrices de encuesta.  Diseña la carga del disco y la relación de transmisión.
x1, x2 = np.meshgrid(xvec, yvec)
```
