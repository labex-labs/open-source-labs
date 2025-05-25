# Empilhando Subplots em Duas Direções

Para criar uma grade de subplots, podemos passar o número de linhas e colunas como argumentos para a função `subplots()`. O objeto `axs` retornado é um array NumPy 2D.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
