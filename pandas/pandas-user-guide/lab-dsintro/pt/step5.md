# Alinhamento de Dados e Aritmética

O alinhamento de dados é uma característica importante do pandas. Quando você realiza operações em dois objetos, o pandas os alinha por seus rótulos associados.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
