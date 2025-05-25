# Largura da Linha Variável

Nesta etapa, criaremos um streamplot com largura de linha variável. O parâmetro `linewidth` controla a largura das linhas de fluxo (streamlines). Aqui, estamos usando o array `speed` que calculamos anteriormente para variar a largura da linha.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
