# Criar o gráfico

Usaremos a visualização de gráfico de barras (barplot) para representar os dados de vendas. Siga estes passos:

1. Crie uma figura e um objeto de eixo usando `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

2. Plote os dados usando o método `barh()` do objeto de eixo.

```python
ax.barh(group_names, group_data)
```
