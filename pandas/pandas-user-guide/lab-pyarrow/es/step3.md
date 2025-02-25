# Usando Tipos de PyArrow con Parámetros

Para los tipos de PyArrow que aceptan parámetros, puedes pasar un tipo de PyArrow con esos parámetros a `ArrowDtype` para usarlo en el parámetro `dtype`.

```python
# Importa PyArrow
import pyarrow as pa

# Crea una Serie de pandas con un tipo de lista de PyArrow
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
