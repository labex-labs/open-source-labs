# Criar subplots

Criaremos uma grade de subplots 2x3 usando a função `subplots()`.

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
