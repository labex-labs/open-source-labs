# Plotar o gráfico

Agora que temos nossos dados de exemplo, podemos plotar o gráfico usando a função `errorbar()`. Passaremos os arrays `x` e `y` como os dois primeiros parâmetros. Em seguida, especificaremos o erro na direção x como 0.2 e o erro na direção y como 0.4, usando os parâmetros `xerr` e `yerr`, respectivamente.

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
