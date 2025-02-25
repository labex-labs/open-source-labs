# Operaciones con PyArrow

La integración de la estructura de datos de PyArrow se implementa a través de la interfaz ExtensionArray de pandas. La funcionalidad admitida existe donde esta interfaz está integrada en la API de pandas.

```python
# Crea una Serie de pandas con un tipo de datos de PyArrow
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# Realiza diversas operaciones
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
