# Criando Eixos Inseridos (Inset Axes)

Nesta etapa, criamos dois eixos inseridos dentro dos eixos do gráfico principal usando `fig.add_axes`. Um exibirá um histograma dos dados, e o outro exibirá a resposta ao impulso (impulse response).

```python
# Create right inset axes
right_inset_ax = fig.add_axes([.65, .6, .2, .2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probability', xticks=[], yticks=[])

# Create left inset axes
left_inset_ax = fig.add_axes([.2, .6, .2, .2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulse response', xlim=(0, .2), xticks=[], yticks=[])
```
