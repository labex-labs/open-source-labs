# Criar um Gráfico

Agora criaremos um gráfico para anotar. O código a seguir criará um gráfico com dois pontos de dados.

```python
fig, ax = plt.subplots()
x = [1, 2]
y = [3, 4]
ax.plot(x, y, "o")
```
