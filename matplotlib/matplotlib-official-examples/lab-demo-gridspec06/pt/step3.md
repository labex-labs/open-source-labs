# Criar a Figura e a Grelha Externa

Em seguida, criaremos a figura e a grelha externa usando a função `add_gridspec`. Criaremos uma grelha 4x4 sem espaçamento entre os subplots.

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
