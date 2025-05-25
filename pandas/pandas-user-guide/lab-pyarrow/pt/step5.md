# Operações PyArrow

A integração da estrutura de dados PyArrow é implementada através da interface ExtensionArray do pandas. A funcionalidade suportada existe onde esta interface está integrada na API do pandas.

```python
# Create a pandas Series with PyArrow data type
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# Perform various operations
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
