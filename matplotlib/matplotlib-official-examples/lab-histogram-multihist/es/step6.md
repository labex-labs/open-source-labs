# Trazar múltiples histogramas

Podemos trazar múltiples histogramas en la misma gráfica pasando una matriz de datos a la función `hist`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```
