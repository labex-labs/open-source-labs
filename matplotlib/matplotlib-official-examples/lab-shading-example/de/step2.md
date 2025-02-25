# Daten laden

Als nächstes laden wir die Beispiel-Daten, die wir in diesem Tutorial verwenden werden. Wir verwenden die Datei `jacksboro_fault_dem.npz`, die Höhen-Daten enthält.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
