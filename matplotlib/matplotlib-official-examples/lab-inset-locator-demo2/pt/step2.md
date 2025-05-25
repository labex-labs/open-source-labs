# Criar uma figura e subplots

Em seguida, criaremos uma figura e subplots para exibir nossos dados. Criaremos dois subplots lado a lado para mostrar dois exemplos diferentes de zooms (insets).

```python
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=[6, 3])
```
