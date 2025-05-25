# Criar o Segundo Gráfico

Em seguida, criaremos o segundo gráfico. Usaremos `subplot` novamente, mas desta vez definiremos o atributo `sharex` para o primeiro gráfico (`ax1`). Isso garante que o segundo gráfico compartilhe o mesmo eixo x que o primeiro gráfico.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
