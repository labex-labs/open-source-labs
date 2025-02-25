# テキストデータを格納する

pandas では、テキストデータを格納する方法は 2 通りあります。`object` 型の NumPy 配列を使用するか、`StringDtype` 拡張型を使用することです。一般的な `object` 型よりも安全で特定性が高いため、`StringDtype` を使用することをお勧めします。

```python
import pandas as pd

# `object` 型でシリーズを作成する
s1 = pd.Series(["a", "b", "c"], dtype="object")

# `StringDtype` でシリーズを作成する
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
