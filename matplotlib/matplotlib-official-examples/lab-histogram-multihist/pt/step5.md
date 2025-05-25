# Personalizar o histograma

Podemos personalizar o histograma alterando a cor, a transparência e a cor da borda das barras usando os parâmetros `color`, `alpha` e `edgecolor`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
