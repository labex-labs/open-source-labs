# Criar os subplots

Criaremos uma figura com dois subplots usando `.pyplot.subplot`.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

A função `subplot()` recebe três argumentos: o número de linhas, o número de colunas e o índice do gráfico atual. O índice começa em 1 no canto superior esquerdo e aumenta linha por linha. Neste exemplo, criamos uma figura com dois subplots: um na parte superior e outro na parte inferior.

No primeiro subplot, plotamos `t1` contra `f(t1)` e `t2` contra `f(t2)`. Definimos a cor do primeiro gráfico como azul e adicionamos marcadores circulares a cada ponto de dados. Definimos a cor do segundo gráfico como preto.

No segundo subplot, plotamos `t2` contra a função cosseno de `2*np.pi*t2`. Definimos a cor do gráfico como laranja e o estilo da linha como tracejado.
