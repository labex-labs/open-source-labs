# Adicionar Tabela ao Gráfico

Adicionaremos uma tabela à parte inferior do gráfico usando a função `plt.table`. Passaremos o texto da célula, os rótulos das linhas, as cores das linhas e os rótulos das colunas como parâmetros para a função.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
