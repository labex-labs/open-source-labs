# Criar o Gráfico

Agora que temos nossos dados, podemos criar nosso gráfico. Começaremos criando um objeto de eixos usando `matplotlib.pyplot.subplots()`. Em seguida, plotaremos nosso primeiro conjunto de dados neste objeto de eixos e definiremos a cor do rótulo como vermelho.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

Em seguida, instanciamos um segundo objeto de eixos que compartilha o mesmo eixo x que o primeiro objeto de eixos usando o método `ax1.twinx()`. Em seguida, plotaremos nosso segundo conjunto de dados neste novo objeto de eixos e definiremos a cor do rótulo como azul.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Finalmente, ajustaremos o layout do nosso gráfico usando o método `fig.tight_layout()` e o exibiremos usando `matplotlib.pyplot.show()`.

```python
fig.tight_layout()
plt.show()
```
