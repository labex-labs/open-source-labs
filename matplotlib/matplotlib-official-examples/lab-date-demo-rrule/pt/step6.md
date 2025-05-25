# Plotar os dados e definir as marcas do eixo x

Finalmente, você pode plotar os dados usando a função `plot` e definir as marcas do eixo x usando as funções de localizador e formatador de marcas que você definiu anteriormente.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
