# 型キャスト規則

提供された入力型に対するコアループ実装がない場合、ufunc の入力に対して型キャストが行われます。キャスト規則は、データ型を安全に別のデータ型にキャストできる時期を決定します。例を見てみましょう。

```python
import numpy as np

# Check if int can be safely cast to float
result = np.can_cast(np.int, np.float)

# Print the result
print(result)
```

出力：

```
True
```
