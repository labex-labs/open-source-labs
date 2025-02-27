# Generar nuevas muestras

Usamos el mejor estimador para tomar 44 nuevos puntos de muestra a partir de los datos. Luego transformamos los nuevos datos de vuelta a sus 64 dimensiones originales usando la inversa de PCA.

```python
# sample 44 new points from the data
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
