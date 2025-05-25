# Plotar Correlação Cruzada

Agora, plotaremos a correlação cruzada entre os dois arrays usando a função `xcorr` em Matplotlib.

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

A função `xcorr` recebe os seguintes parâmetros:

- `x`: o primeiro array de dados
- `y`: o segundo array de dados
- `usevlines`: booleano, se deve plotar linhas verticais de 0 ao valor da correlação
- `maxlags`: inteiro, o número máximo de lags para calcular a correlação
- `normed`: booleano, se deve normalizar os valores da correlação
- `lw`: inteiro, a largura da linha para o gráfico
