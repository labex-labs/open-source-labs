# Criar dois histogramas com barras empilhadas

Podemos criar dois histogramas com barras empilhadas chamando a função `hist` duas vezes e definindo o parâmetro `histtype` como `'barstacked'`. Neste exemplo, criaremos dois histogramas com barras empilhadas.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
