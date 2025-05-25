# Criar o Primeiro Gráfico

Agora, vamos criar o primeiro gráfico usando `subplot`. `subplot` recebe três argumentos: o número de linhas, o número de colunas e o número do gráfico. Neste exemplo, criaremos um gráfico com 2 linhas e 1 coluna (`211`), o que significa que o primeiro gráfico estará na linha superior.

```python
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
```
