# Criar Figura e Subplots

Criaremos uma figura com dois subplots usando o método `add_gridspec`.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```
