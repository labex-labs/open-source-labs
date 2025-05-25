# Criar Figura e Eixos

Em seguida, criaremos uma figura e eixos usando o método `subplots()`. Em seguida, plotaremos duas linhas nos eixos e adicionaremos uma legenda para distingui-las.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
