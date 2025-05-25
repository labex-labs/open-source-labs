# Criar os ImageGrids

Criaremos dois ImageGrids para exibir nossas imagens. O primeiro ImageGrid terá duas linhas e duas colunas, e o segundo ImageGrid também terá duas linhas e duas colunas.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
