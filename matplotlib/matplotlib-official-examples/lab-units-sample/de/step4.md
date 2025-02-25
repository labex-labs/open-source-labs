# Erstellen des Plots

Erstellen Sie ein 2x2-Gitter von Teilplots mit der Funktion `subplots`. Verwenden Sie dann die Funktion `plot`, um die Daten in jedem Teilplot zu plotten.

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # Skalare werden in den aktuellen Maßeinheiten interpretiert

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # cm werden in Zoll umgerechnet
```
