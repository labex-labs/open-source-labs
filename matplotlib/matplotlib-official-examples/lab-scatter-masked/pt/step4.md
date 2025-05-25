# Adicionando uma Linha para Demarcar as Regiões Mascaradas

Finalmente, adicionamos uma linha para demarcar as regiões mascaradas. Criamos um array de valores theta e plotamos um círculo com raio `r0` usando `np.cos(theta)` e `np.sin(theta)`.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
