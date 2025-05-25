# Plotar usando `.step()`

Podemos usar a função `.step()` para criar curvas constantes por partes. O parâmetro `where` determina onde os degraus devem ser desenhados. Criaremos três gráficos usando diferentes valores para `where`.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

O código acima criará um gráfico com três curvas constantes por partes, cada uma com um valor diferente para `where`.
