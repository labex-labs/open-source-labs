# 構造化配列の作成

構造化配列を作成するには、`np.array` 関数を使用して、`dtype` パラメータを使ってデータ型を指定します。データ型はタプルのリストでなければならず、各タプルは構造化配列のフィールドを表します。各タプルには、フィールド名とそのフィールドのデータ型が含まれている必要があります。

```python
import numpy as np

# Create a structured array
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
