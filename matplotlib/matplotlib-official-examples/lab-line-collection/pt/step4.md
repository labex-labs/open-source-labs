# Criar o Gráfico

Agora podemos criar um gráfico usando `matplotlib` e adicionar o objeto `LineCollection` ao gráfico usando o método `add_collection` do objeto `Axes`.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
