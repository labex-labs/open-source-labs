# Adicionar anotação de seta com unidades mistas

Nesta etapa, adicionaremos outra anotação de seta ao gráfico usando a função `annotate()`. Forneceremos a posição da seta, o texto a ser exibido e as propriedades da seta. Também misturaremos unidades de medida para a posição e usaremos a fração dos eixos para o texto.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
