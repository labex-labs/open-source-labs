# Plotar Dados em Subfiguras

Para plotar dados nas subfiguras, você precisa criar um subplot para cada subfigura usando `subfig.subplots()`. Em seguida, você pode usar qualquer uma das funções de plotagem em Matplotlib para criar os gráficos.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

Isso criará duas subfiguras, cada uma com um gráfico de dados aleatórios.
