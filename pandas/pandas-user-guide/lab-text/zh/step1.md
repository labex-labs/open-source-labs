# 存储文本数据

在pandas中，你可以通过两种方式存储文本数据：使用`object`数据类型的NumPy数组或`StringDtype`扩展类型。我们建议使用`StringDtype`，因为它比通用的`object`数据类型更安全、更具针对性。

```python
import pandas as pd

# 创建一个具有`object`数据类型的序列
s1 = pd.Series(["a", "b", "c"], dtype="object")

# 创建一个具有`StringDtype`的序列
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
