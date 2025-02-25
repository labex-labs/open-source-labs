# Cargar datos de EEG y graficar trazas

El siguiente paso es cargar los datos de EEG y graficar las trazas. Utilizaremos la función `fromfile()` para cargar los datos de un archivo y `LineCollection()` para graficar las trazas. También estableceremos las etiquetas de las marcas de la escala en el eje y para los canales de electrodos.

```python
# Cargar los datos de EEG
n_samples, n_rows = 800, 4
data = np.load('eeg_data.npy')
t = 10 * np.arange(n_samples) / n_samples

# Graficar los datos de EEG
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(10))
dmin = data.min()
dmax = data.max()
dr = (dmax - dmin) * 0.7  # Apretarlas un poco.
y0 = dmin
y1 = (n_rows - 1) * dr + dmax
ax2.set_ylim(y0, y1)

segs = []
for i in range(n_rows):
    segs.append(np.column_stack((t, data[:, i])))

offsets = np.zeros((n_rows, 2), dtype=float)
offsets[:, 1] = np.arange(n_rows) * dr

lines = LineCollection(segs, offsets=offsets, transOffset=None)
ax2.add_collection(lines)

# Establecer las marcas de la escala en el eje y para usar coordenadas de los ejes en el eje y
ax2.set_yticks(offsets[:, 1])
ax2.set_yticklabels(['PG3', 'PG5', 'PG7', 'PG9'])
ax2.set_xlabel('Tiempo (s)')
```
