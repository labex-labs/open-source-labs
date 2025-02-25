# Personalizar el histograma

Podemos personalizar el histograma cambiando el color, la transparencia y el color del borde de las barras utilizando los parámetros `color`, `alpha` y `edgecolor`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
