# Criar um Gráfico de Dados Negativos e Colorbar

Criamos um gráfico dos dados negativos e adicionamos uma colorbar ao gráfico usando a função `colorbar`. Desta vez, especificamos a localização da colorbar, bem como os parâmetros `anchor` e `shrink`.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
