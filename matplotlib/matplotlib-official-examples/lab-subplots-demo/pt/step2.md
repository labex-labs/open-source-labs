# Empilhando Subplots em Uma Direção

Para criar múltiplos subplots empilhados verticalmente ou horizontalmente, podemos passar o número de linhas e colunas como argumentos para a função `subplots()`. O objeto `axs` retornado é um array numpy 1D contendo a lista de `Axes` criados.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
