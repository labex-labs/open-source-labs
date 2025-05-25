# Alterar o estilo do histograma

Podemos alterar o estilo do histograma especificando o parâmetro `histtype` na função `hist`. Neste exemplo, criaremos um histograma com uma curva de passo (step curve) que possui um preenchimento de cor.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
