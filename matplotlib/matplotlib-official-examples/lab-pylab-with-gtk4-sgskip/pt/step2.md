# Criar a figura e os gráficos

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

Criamos uma figura com dois subplots e plotamos dois conjuntos de dados nela. Também adicionamos uma legenda aos gráficos.
