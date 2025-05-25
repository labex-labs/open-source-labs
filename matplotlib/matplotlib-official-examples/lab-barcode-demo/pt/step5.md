# Renderizar o Código de Barras

Finalmente, podemos renderizar o código de barras usando `Axes.imshow`. Usaremos `code.reshape(1, -1)` para transformar os dados em um array 2D com uma linha, `imshow(..., aspect='auto')` para permitir pixels não quadrados e `imshow(..., interpolation='nearest')` para evitar bordas borradas.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
