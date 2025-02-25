# Graficar datos en subfiguras

Para graficar datos en las subfiguras, debes crear un subgráfico para cada subfigura usando `subfig.subplots()`. Luego, puedes usar cualquiera de las funciones de graficación en Matplotlib para crear los gráficos.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

Esto creará dos subfiguras, cada una con un gráfico de datos aleatorios.
