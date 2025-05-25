# Criar o Gráfico Inicial

Em seguida, criamos o gráfico inicial que será atualizado com base na entrada do usuário. Neste exemplo, criamos um gráfico de uma função com `t` como a variável independente.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
