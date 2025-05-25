# Usando Tipos PyArrow com Parâmetros

Para tipos PyArrow que aceitam parâmetros, você pode passar um tipo PyArrow com esses parâmetros para `ArrowDtype` para usar no parâmetro `dtype`.

```python
# Import PyArrow
import pyarrow as pa

# Create a pandas Series with PyArrow list type
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
