# 日付時刻の目盛りを扱う

x 軸に日付時刻の値を使用する場合、適切な日付のロケータとフォーマッタを取得するために、文字列を日付時刻オブジェクトに変換することが重要です。以下は例です：

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with datetime strings
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convert strings to datetime64
x = np.asarray(x, dtype='datetime64[s]')

# plot the data with datetime tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

この例では、`np.asarray()` を使用して文字列を datetime64 に変換しています。再度データをプロットすると、目盛りのラベルは期待通りになります。
