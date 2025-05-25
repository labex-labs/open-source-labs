# Criar o Gráfico de Quiver

Podemos criar o gráfico de quiver usando a função `ax.quiver()`. Passamos os arrays `X`, `Y`, `U` e `V` como parâmetros.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
