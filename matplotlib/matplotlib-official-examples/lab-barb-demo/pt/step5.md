# Criar o Gráfico de "Wind Barb" Mascarado

Também podemos criar um gráfico de "wind barb" mascarado usando um array mascarado. Neste caso, mudaremos o valor de um vetor para um valor inválido e o mascararemos.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Bad value that should not be plotted when masked
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
