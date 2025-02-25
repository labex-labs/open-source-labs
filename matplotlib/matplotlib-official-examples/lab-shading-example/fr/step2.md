# Charger les données

Ensuite, nous allons charger les données d'échantillonnage que nous utiliserons pour ce tutoriel. Nous utiliserons le fichier `jacksboro_fault_dem.npz`, qui contient des données d'altitude.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
