# Resaltando ciertas regiones con `where`

El argumento de palabras clave `where` es muy útil para resaltar ciertas regiones del gráfico. `where` toma una máscara booleana de la misma longitud que los argumentos x, ymin y ymax, y solo rellena la región donde la máscara booleana es True. En el ejemplo siguiente, simulamos un solo caminante aleatorio y calculamos la media y desviación estándar analítica de las posiciones de la población. La media de la población se muestra como una línea discontinua, y la desviación más/menos una sigma a partir de la media se muestra como la región rellena. Utilizamos la máscara where `X > upper_bound` para encontrar la región donde el caminante está fuera del límite de una sigma, y sombreada esa región de color rojo.

```python
# Fixing random state for reproducibility
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# los pasos y la posición
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# los límites analíticos inferiores y superiores de una sigma de la población
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='posición del caminante')
ax.plot(t, mu*t, lw=1, label='media de la población', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='rango de una sigma')
ax.legend(loc='upper left')

# aquí usamos el argumento where para solo rellenar la región donde el
# caminante está por encima del límite de una sigma de la población
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('número de pasos')
ax.set_ylabel('posición')
ax.grid()
```
