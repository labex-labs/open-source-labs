# Criar a figura e os subplots

Nesta etapa, criaremos uma figura com dois subplots para as distribuições cumulativas. Também definiremos o tamanho da figura para 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
