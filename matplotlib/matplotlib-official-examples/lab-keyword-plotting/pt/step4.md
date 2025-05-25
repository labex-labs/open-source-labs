# Gerar o Gráfico

Nesta etapa, geraremos um gráfico de dispersão (scatter plot) usando o dicionário `data` como entrada para a função `scatter()`. Usaremos as strings correspondentes às variáveis `a`, `b`, `c` e `d` para gerar o gráfico.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
```
