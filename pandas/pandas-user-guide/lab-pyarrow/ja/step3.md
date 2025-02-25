# パラメータ付きの PyArrow 型の使用

パラメータを受け取る PyArrow 型の場合、それらのパラメータ付きの PyArrow 型を `ArrowDtype` に渡して、`dtype` パラメータで使用することができます。

```python
# PyArrow をインポート
import pyarrow as pa

# PyArrow のリスト型を持つ pandas の Series を作成
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
