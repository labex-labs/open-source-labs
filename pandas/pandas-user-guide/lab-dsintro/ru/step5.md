# Выравнивание данных и арифметические операции

Выравнивание данных — важная особенность pandas. При выполнении операций с двумя объектами pandas выравнивает их по связанным меткам.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
