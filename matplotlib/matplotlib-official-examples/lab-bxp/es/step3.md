# Personalizar las estadísticas del diagrama de caja

Podemos modificar cualquiera de las estadísticas del diagrama de caja que se calcularon en el Paso 2. En este ejemplo, establecemos la mediana de cada conjunto en la mediana de todos los datos y duplicamos las medias.

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```
