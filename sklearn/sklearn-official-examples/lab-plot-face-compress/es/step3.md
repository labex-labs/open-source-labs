# Consumo de memoria

Ahora comprobaremos el uso de memoria de las imágenes comprimidas. Esperamos que la imagen comprimida ocupe 8 veces menos memoria que la imagen original.

```python
print(f"El número de bytes ocupados en la RAM es {compressed_raccoon_kmeans.nbytes}")
print(f"Ratio de compresión: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
