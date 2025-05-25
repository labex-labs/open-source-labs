# Preparar os Dados

Os dados para o gráfico são preparados nesta etapa. Criaremos uma lista com os nomes das pessoas, seu desempenho e a taxa de erro.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
