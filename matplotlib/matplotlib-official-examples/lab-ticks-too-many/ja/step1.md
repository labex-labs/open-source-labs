# データ型を確認する

最初のステップは、x 軸の値のデータ型を確認することです。文字列のリストである場合、目盛りの挙動が予期しないものになる可能性があります。これを修正するには、文字列を数値型に変換する必要があります。以下は例です：

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Categories')
plt.show()
```

この例では、x 軸に文字列のリストがあります。データをプロットすると、目盛りのラベルが順序通りでなく配置が不適切になります。
