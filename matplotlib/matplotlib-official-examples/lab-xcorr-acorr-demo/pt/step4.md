# Plotar Autocorrelação

Agora, plotaremos a autocorrelação do array `x` usando a função `acorr` em Matplotlib.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

A função `acorr` recebe os seguintes parâmetros:

- `x`: o array de dados para calcular a autocorrelação
- `usevlines`: booleano, se deve plotar linhas verticais de 0 ao valor da correlação
- `normed`: booleano, se deve normalizar os valores da correlação
- `maxlags`: inteiro, o número máximo de lags para calcular a correlação
- `lw`: inteiro, a largura da linha para o gráfico
