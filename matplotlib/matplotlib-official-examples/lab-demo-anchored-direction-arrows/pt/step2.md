# Criar um gráfico

Em seguida, criaremos um gráfico simples usando NumPy. Este gráfico servirá como plano de fundo para as setas direcionais ancoradas.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
