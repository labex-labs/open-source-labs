# グラフを作成する

次に、操作対象となるシンプルなグラフを作成しましょう。グラフにプロットするランダムデータを生成するために NumPy を使用します。

```python
import numpy as np

# Generate random data
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Create the plot
fig, ax = plt.subplots()
ax.plot(data)
```
