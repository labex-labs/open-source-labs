# Criar Dados Artificiais

Precisamos criar alguns dados artificiais para plotar. Neste laboratório, plotaremos o logaritmo da frequência (em Hz) contra o logaritmo da potência (em Watts). Usaremos a biblioteca `numpy` para gerar os dados.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
