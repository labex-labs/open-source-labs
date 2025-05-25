# Visualizar os Dados

Vamos visualizar os dados gerados usando um gráfico de dispersão.

```python
# Plotar os pontos de dados
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()
```
