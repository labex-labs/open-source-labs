# Zentrierte Koordinaten

Oft möchte ein Benutzer _X_ und _Y_ mit der gleichen Größe wie _Z_ an `.axes.Axes.pcolormesh` übergeben. Dies ist auch möglich, wenn `shading='auto'` übergeben wird (Standardwert, der von :rc:`pcolor.shading` gesetzt wird). Vor Matplotlib 3.3 hätte `shading='flat'` die letzte Spalte und Zeile von _Z_ weggelassen, aber jetzt wird ein Fehler ausgegeben. Wenn das wirklich das ist, was Sie möchten, können Sie einfach die letzte Zeile und Spalte von Z manuell weglassen:

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # Länge = 10
y = np.arange(6)  # Länge = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
