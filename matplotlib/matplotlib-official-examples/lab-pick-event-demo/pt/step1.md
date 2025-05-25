# Seleção Simples, Linhas, Retângulos e Texto

Começaremos habilitando a seleção simples definindo a propriedade "picker" de um _artist_ (elemento gráfico). Isso permitirá que o _artist_ dispare um evento de seleção se o evento do mouse estiver sobre o _artist_. Criaremos um gráfico simples contendo uma linha, um retângulo e texto, e habilitaremos a seleção em cada um desses _artists_.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Pick the rectangle.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Make the xtick labels pickable.
    label.set_picker(True)
```
