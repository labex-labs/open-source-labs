# Plotar histogramas de passos

Podemos plotar histogramas de passos definindo o parâmetro `histtype` como `'step'`.

```python
plt.hist(x, n_bins, histtype='step', color=['green', 'blue', 'red'], label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Step Histogram of Random Data')
plt.legend()
plt.show()
```
