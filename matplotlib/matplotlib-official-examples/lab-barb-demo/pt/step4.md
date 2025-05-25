# Personalizar o Gráfico de "Wind Barb"

Podemos personalizar o gráfico de "wind barb" alterando os parâmetros da função `barbs`. Por exemplo, podemos alterar o comprimento e o ponto de pivô dos vetores, preencher os círculos para um "barb" vazio e alterar as cores das bandeiras e barras.

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
