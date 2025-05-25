# Adicionar uma Barra de Tamanho

Desenhe uma barra horizontal com um comprimento de 0.1 em coordenadas de dados, com um rótulo fixo abaixo.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
