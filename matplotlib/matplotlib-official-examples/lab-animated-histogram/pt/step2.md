# Definir Semente Aleatória e Bins

Defina a semente aleatória para reprodutibilidade e fixe as bordas dos bins.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```
