# PyArrow の操作

PyArrow のデータ構造の統合は、pandas の ExtensionArray インターフェイスを通じて実装されています。このインターフェイスが pandas API 内に統合されている場所には、サポートされる機能が存在します。

```python
# PyArrow データ型を持つ pandas の Series を作成
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# 様々な操作を実行
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
