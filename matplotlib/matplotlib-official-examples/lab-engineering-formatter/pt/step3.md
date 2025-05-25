# Criar a Figura e os Subplots

Precisamos criar uma figura e subplots para exibir os dados. Neste laboratório, criaremos dois subplots, lado a lado.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
