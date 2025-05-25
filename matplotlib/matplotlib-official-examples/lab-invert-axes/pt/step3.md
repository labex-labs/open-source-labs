# Criar o Gráfico

Agora, podemos criar o gráfico usando Matplotlib. Usaremos a função `plot` para plotar nossos dados e definir os limites do eixo x usando a função `set_xlim`.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
