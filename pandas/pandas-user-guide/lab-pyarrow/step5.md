# PyArrow Operations

PyArrow data structure integration is implemented through pandas' ExtensionArray interface. Supported functionality exists where this interface is integrated within the pandas API.

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
