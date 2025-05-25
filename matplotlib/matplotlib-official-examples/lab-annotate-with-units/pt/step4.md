# Adicionar anotação de seta com xy unitizado e texto

Nesta etapa, adicionaremos uma anotação de seta ao gráfico usando a função `annotate()`. Forneceremos a posição da seta, o texto a ser exibido e as propriedades da seta. Também especificaremos as unidades de medida para a posição e o texto.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
