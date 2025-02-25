# 文字列を数値型に変換する

目盛りの挙動を修正するには、文字列を数値型に変換する必要があります。以下は例です：

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convert strings to floats
x = np.asarray(x, dtype='float')

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

この例では、`np.asarray()` を使用して文字列を浮動小数点数に変換しています。再度データをプロットすると、目盛りのラベルは期待通りになります。
