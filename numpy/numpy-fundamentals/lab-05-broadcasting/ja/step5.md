# ブロードキャストの例

ブロードキャストがさまざまなシナリオでどのように機能するかを理解するために、いくつかの例を見てみましょう。

- 例 1：

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])
result = a + b
```

この場合、`b` が `a` の各行に加算されます。結果は `a` と同じ形状の 2 次元配列で、各要素は `a` と `b` の対応する要素の和になっています。

- 例 2：

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0])
result = a + b
```

この場合、ブロードキャストが失敗します。なぜなら、`a` と `b` の末尾の次元が等しくないからです。要素ごとの加算のために、`a` の行の値を `b` の要素と整列させることは不可能です。
