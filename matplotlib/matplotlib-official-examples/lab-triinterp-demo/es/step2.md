# Interpolar datos usando el método lineal

El segundo paso es interpolar los datos usando el método lineal. Crearemos una malla cuadrada con espaciado regular y luego usaremos el método LinearTriInterpolator para interpolar los datos. Finalmente, graficaremos los datos interpolados.

```python
# Interpolar a una malla cuadrada con espaciado regular.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpolar usando el método lineal.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Graficar los datos interpolados.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```
