# Laden der Daten

Als nächstes laden wir die Beispielhöhendaten mit der Funktion `get_sample_data` aus Matplotlib. Anschließend extrahieren wir die Höheninformationen und die Zellengröße des Gitters.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
