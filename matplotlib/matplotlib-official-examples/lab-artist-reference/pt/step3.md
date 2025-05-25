# Desenhar Formas

Agora desenharemos as formas usando Matplotlib, iterando pela lista `shapes` e adicionando-as ao gráfico.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
