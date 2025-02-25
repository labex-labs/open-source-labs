# Charger les données

Ensuite, nous chargeons les données d'altitude d'échantillonnage à l'aide de la fonction `get_sample_data` de Matplotlib. Nous extrayons ensuite les données d'altitude et la taille des cellules de la grille.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
