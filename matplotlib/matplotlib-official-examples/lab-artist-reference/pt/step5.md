# Salvar o Gráfico

Podemos salvar o gráfico como um arquivo de imagem usando a função `savefig`.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.savefig('shapes.png')
```
