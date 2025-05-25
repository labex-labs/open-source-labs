# Criar um Gráfico Simples de Barras de Erro

Criaremos um gráfico simples de barras de erro com barras de erro padrão usando a função `errorbar`. Aqui, definiremos os valores x e y, juntamente com seus valores de erro correspondentes. Também definiremos o estilo da linha como pontilhado.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
