# Gráfico de dispersão com o modo autolimit_mode round_numbers

Nesta etapa, mudaremos `axes.autolimit_mode` para 'round_numbers' e criaremos um gráfico de dispersão para manter os ticks em números arredondados e também ter ticks nas bordas.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
