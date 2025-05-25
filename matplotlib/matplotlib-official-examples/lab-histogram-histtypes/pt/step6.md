# Criar um histograma com larguras de bin personalizadas

Podemos criar um histograma com larguras de bin personalizadas e desiguais fornecendo uma lista de bordas de bin (bin edges). Neste exemplo, criaremos um histograma com bins espaçados de forma desigual.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
