# Teilmengen von Diagrammen erstellen

Wir werden ein 2x3-Gitter von Teilmengen von Diagrammen mit der Funktion `subplots()` erstellen.

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
