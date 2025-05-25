# Criando Subplots para Cada Coluna

Podemos criar subplots separados para cada uma das colunas de dados usando o argumento `subplots`.

```python
# Criando subplots para cada coluna
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
