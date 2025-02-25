# Diagramme erstellen

Jetzt werden wir drei Teilbilder mit der Funktion `plt.subplots` erstellen. Zwei Diagramme werden in einer Figur erstellt, während das dritte Diagramm in einer separaten Figur erstellt wird.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
