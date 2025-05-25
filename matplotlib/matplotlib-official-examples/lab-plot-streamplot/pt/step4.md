# Cor Variável

Nesta etapa, criaremos um streamplot com cor variável. O parâmetro `color` recebe um array 2D que representa a magnitude do campo vetorial. Aqui, estamos usando o componente `U` do campo vetorial como a cor.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
