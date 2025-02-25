# Especificar la fuente de luz y la paleta de colores

Especificamos el objeto LightSource estableciendo la azimuth y la altitude de la fuente de luz. También establecemos la paleta de colores que se utilizará en la gráfica.

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
