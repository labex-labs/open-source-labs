# データ構造の統合

PyArrow を使うと、pandas のデータ構造を NumPy 配列と同様に PyArrow ChunkedArray で直接バックアップすることができます。方法は以下の通りです。

```python
# pandas をインポート
import pandas as pd

# PyArrow データ型を持つ pandas の Series、Index、DataFrame を作成
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
