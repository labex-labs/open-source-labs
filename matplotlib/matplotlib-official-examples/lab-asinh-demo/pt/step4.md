# Comparar o comportamento de "symlog" e "asinh" no gráfico de amostra y=x

Vamos comparar o comportamento de "symlog" e "asinh" em um gráfico de amostra y=x. Plotaremos o mesmo gráfico duas vezes, uma vez com "symlog" e outra com "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
