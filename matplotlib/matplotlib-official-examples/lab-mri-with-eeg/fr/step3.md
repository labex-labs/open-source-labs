# Charger les données EEG et tracer les traces

L'étape suivante consiste à charger les données EEG et à tracer les traces. Nous utiliserons la fonction `fromfile()` pour charger les données à partir d'un fichier et `LineCollection()` pour tracer les traces. Nous définirons également les étiquettes d'échelle sur l'axe des y pour les canaux d'électrodes.

```python
# Charger les données EEG
n_samples, n_rows = 800, 4
data = np.load('eeg_data.npy')
t = 10 * np.arange(n_samples) / n_samples

# Tracer les données EEG
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(10))
dmin = data.min()
dmax = data.max()
dr = (dmax - dmin) * 0.7  # Les espacer un peu.
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

# Définir les échelles y pour utiliser les coordonnées des axes sur l'axe des y
ax2.set_yticks(offsets[:, 1])
ax2.set_yticklabels(['PG3', 'PG5', 'PG7', 'PG9'])
ax2.set_xlabel('Temps (s)')
```
