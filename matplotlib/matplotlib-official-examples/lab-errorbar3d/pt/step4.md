# Adicionar Barras de Erro ao Gráfico

Adicionamos barras de erro ao nosso gráfico usando o método `errorbar` do objeto `Axes3D`. Definimos os parâmetros `zuplims` e `zlolims` como arrays que especificam quais pontos de dados têm limites superiores e inferiores. Definimos o parâmetro `errorevery` para controlar a frequência das barras de erro.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
