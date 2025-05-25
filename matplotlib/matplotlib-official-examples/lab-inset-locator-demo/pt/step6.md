# Criar um _Inset_ Fora dos Eixos

Podemos criar um _inset_ fora dos eixos usando o parâmetro `bbox_to_anchor` para especificar uma caixa delimitadora em coordenadas dos eixos que se estende para fora dos eixos.

```python
# Criar um inset fora dos eixos
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05, .6, .5, .4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
