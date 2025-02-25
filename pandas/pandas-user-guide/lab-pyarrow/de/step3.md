# Verwenden von PyArrow-Typen mit Parametern

Für PyArrow-Typen, die Parameter akzeptieren, können Sie einen PyArrow-Typ mit diesen Parametern in `ArrowDtype` übergeben, um ihn im `dtype`-Parameter zu verwenden.

```python
# Importiere PyArrow
import pyarrow as pa

# Erstelle eine pandas-Serie mit PyArrow-Liste-Typ
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
