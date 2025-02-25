# Crear el eje y secundario

Crearemos un tercer ejemplo de relación entre los ejes en una transformación que es ad-hoc a partir de los datos y se deriva empíricamente. En este caso, estableceremos las funciones de transformación directa e inversa para ser interpolaciones lineales de un conjunto de datos al otro.

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Datos trazados')

xold = np.arange(0, 11, 0.2)
# Conjunto de datos ficticio que relaciona la coordenada x con otra coordenada derivada de los datos.
# xnew debe ser monotónico, así que lo ordenamos...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Datos de transformación')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{otro}$')
```
