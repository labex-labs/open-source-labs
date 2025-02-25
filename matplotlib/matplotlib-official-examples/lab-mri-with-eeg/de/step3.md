# EEG-Daten laden und Spuren plotten

Der nächste Schritt besteht darin, die EEG-Daten zu laden und die Spuren zu plotten. Wir werden die `fromfile()`-Funktion verwenden, um die Daten aus einer Datei zu laden, und `LineCollection()`, um die Spuren zu plotten. Wir werden auch die y-Achsenmarkierungen auf die Elektrodenkanäle setzen.

```python
# Lade die EEG-Daten
n_samples, n_rows = 800, 4
data = np.load('eeg_data.npy')
t = 10 * np.arange(n_samples) / n_samples

# Plotte die EEG-Spuren
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(10))
dmin = data.min()
dmax = data.max()
dr = (dmax - dmin) * 0.7  # Platzieren Sie sie ein wenig enger.
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

# Setze die y-Achsenmarkierungen, um die Achsenkoordinaten auf der y-Achse zu verwenden
ax2.set_yticks(offsets[:, 1])
ax2.set_yticklabels(['PG3', 'PG5', 'PG7', 'PG9'])
ax2.set_xlabel('Zeit (s)')
```
