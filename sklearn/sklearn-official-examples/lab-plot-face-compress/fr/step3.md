# Emprise mémoire

Nous allons maintenant vérifier l'utilisation mémoire des images compressées. Nous nous attendons à ce que l'image compressée prenne 8 fois moins de mémoire que l'image originale.

```python
print(f"Le nombre d'octets occupés en RAM est {compressed_raccoon_kmeans.nbytes}")
print(f"Taux de compression : {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
