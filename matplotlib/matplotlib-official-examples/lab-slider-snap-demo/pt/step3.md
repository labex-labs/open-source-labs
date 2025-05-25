# Criar a Figura e os Eixos

Nesta etapa, você criará a figura e os eixos para o gráfico. Você também ajustará a posição dos eixos para abrir espaço para os _sliders_.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```
