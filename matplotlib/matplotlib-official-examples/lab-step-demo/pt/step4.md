# Plotar usando `.plot()`

Podemos obter o mesmo comportamento que `.step()` usando o parâmetro `drawstyle` da função `.plot()`. Criaremos três gráficos usando diferentes valores para `drawstyle`.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

O código acima criará um gráfico com três curvas constantes por partes, cada uma com um valor diferente para `drawstyle`.
