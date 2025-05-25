# Criar _Insets_ com Posições Arbitrárias

Podemos criar _insets_ com posições arbitrárias usando o parâmetro `bbox_to_anchor` para especificar uma caixa delimitadora em coordenadas de dados e usando o parâmetro `bbox_transform` para especificar a transformação para a caixa delimitadora.

```python
# Criar inset em coordenadas de dados usando ax.transData como transformação
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
