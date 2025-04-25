# 散布図の作成

Matplotlib を使って散布図を作成することもできます。この例では、x と y の値の関係を示す散布図を作成します。

```python
import matplotlib.pyplot as plt

# x 軸の値
x = [1, 2, 3, 4, 5]

# y 軸の値
y = [2, 4, 6, 8, 10]

# 点を描画
plt.scatter(x, y)

# タイトルを設定
plt.title("Simple Scatter Plot")

# x 軸のラベルを設定
plt.xlabel("X-axis")

# y 軸のラベルを設定
plt.ylabel("Y-axis")

# グラフを表示
plt.show()
```
