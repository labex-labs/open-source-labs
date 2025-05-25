# 매개변수와 함께 PyArrow 타입 사용하기

매개변수를 허용하는 PyArrow 타입의 경우, 해당 매개변수를 사용하여 PyArrow 타입을 `ArrowDtype`에 전달하여 `dtype` 매개변수에서 사용할 수 있습니다.

```python
# Import PyArrow
import pyarrow as pa

# Create a pandas Series with PyArrow list type
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
