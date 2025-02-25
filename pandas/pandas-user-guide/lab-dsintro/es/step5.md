# Alineamiento de datos y aritmética

El alineamiento de datos es una característica importante de pandas. Cuando realizas operaciones en dos objetos, pandas los alinea por sus etiquetas asociadas.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
