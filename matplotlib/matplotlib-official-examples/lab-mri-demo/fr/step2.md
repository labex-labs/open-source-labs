# Charger les données d'image IRM

Nous allons utiliser la fonction `get_sample_data` de `matplotlib` pour charger l'image IRM d'échantillonnage. L'image est au format entier 16 bits de 256x256.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
