# Erzeuge eine Figur und füge eine Hauptachse hinzu

Wir erstellen eine Figur mit der `plt.figure()`-Methode und fügen eine Hauptachse hinzu mit der `fig.add_axes()`-Methode. Die Hauptachse teilt die x-Skala mit der Parasitenachse.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
