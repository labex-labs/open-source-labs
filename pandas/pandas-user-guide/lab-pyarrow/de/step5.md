# PyArrow-Operationen

Die Integration von PyArrow-Datenstrukturen erfolgt über die ExtensionArray-Schnittstelle von pandas. Unterstützte Funktionalität besteht dort, wo diese Schnittstelle innerhalb der pandas-API integriert ist.

```python
# Erstelle eine pandas-Serie mit PyArrow-Datentyp
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# Führe verschiedene Operationen durch
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
