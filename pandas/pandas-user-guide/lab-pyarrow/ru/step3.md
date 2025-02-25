# Использование типов PyArrow с параметрами

Для типов PyArrow, которые принимают параметры, вы можете передать в `ArrowDtype` PyArrow-тип с этими параметрами для использования в параметре `dtype`.

```python
# Импортировать PyArrow
import pyarrow as pa

# Создать pandas Series с типом списка PyArrow
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
