# Criar um Gráfico de Barras com Hachuras

Agora que você tem seus dados, pode criar um gráfico de barras com hachuras (hatching). Você pode usar hachuras para criar padrões nas barras do seu gráfico. Neste caso, usaremos o parâmetro `hatch` para adicionar hachuras às nossas barras.

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
