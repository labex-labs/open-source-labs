# Erstellen eines Beispiel-Diagramms

Lassen Sie uns ein Beispiel-Diagramm erstellen, um zu sehen, wie es mit den Tick-Labels der y-Achse auf der rechten Seite aussieht.

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
