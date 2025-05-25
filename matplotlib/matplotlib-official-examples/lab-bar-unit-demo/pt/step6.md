# Adicionar Rótulos e Título ao Gráfico

O passo final é adicionar rótulos e um título ao gráfico. Adicionaremos um título ao gráfico, um rótulo para o eixo x e uma legenda para o gráfico.

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```
