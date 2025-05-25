# Especificar a Fonte de Luz e o Mapa de Cores

Especificamos o objeto `LightSource` definindo o azimute e a altitude da fonte de luz. Também definimos o mapa de cores a ser usado no gráfico.

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
