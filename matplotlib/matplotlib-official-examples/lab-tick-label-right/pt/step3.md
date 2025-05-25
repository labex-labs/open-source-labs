# Criar um gráfico de exemplo

Vamos criar um gráfico de exemplo para ver como ele fica com os rótulos de marcação do eixo y no lado direito.

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
