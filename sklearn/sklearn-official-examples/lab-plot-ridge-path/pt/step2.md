# Gerar Dados

Neste passo, geraremos uma matriz de Hilbert 10x10 e definiremos a variável alvo y como um vetor de uns.

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
