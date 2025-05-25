# Configurar o Gráfico

Agora, podemos configurar o gráfico. Usaremos `plt.subplots()` para criar um objeto de figura e eixo. Em seguida, usaremos `ax.triplot()` para plotar a triangulação.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
