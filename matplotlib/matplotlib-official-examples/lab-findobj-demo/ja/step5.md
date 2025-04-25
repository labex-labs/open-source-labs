# さまざまな種類のグラフの作成

Matplotlib は、線グラフ、散布図、棒グラフなど、幅広い種類のグラフをサポートしています。以下は、散布図を作成するコード例です。

```python
import matplotlib.pyplot as plt
import numpy as np

# いくつかのランダムなデータを生成する
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# 散布図を作成する
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# ラベルとタイトルを追加する
plt.xlabel('X 軸')
plt.ylabel('Y 軸')
plt.title('散布図')

# グラフを表示する
plt.show()
```

このコードでは、`scatter()` メソッドを使用して散布図を作成しています。NumPy ライブラリを使っていくつかのランダムなデータを生成し、それを `scatter()` メソッドに渡しています。また、`c` パラメータを使ってデータポイントの色を指定し、`s` パラメータを使ってデータポイントのサイズを指定し、`alpha` パラメータを使ってデータポイントの透明度を指定しています。
