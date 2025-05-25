# Criar um Subplot

Criaremos um subplot para mostrar os segmentos de linha coloridos. Usaremos a função `subplots` de `matplotlib.pyplot` para criar uma grade de subplots 2x1, e os parâmetros `sharex` e `sharey` para compartilhar os eixos x e y entre os subplots.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
