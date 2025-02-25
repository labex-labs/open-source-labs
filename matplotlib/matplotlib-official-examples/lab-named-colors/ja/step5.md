# 棒グラフの作成

Matplotlib を使って棒グラフを作成することもできます。この例では、売れたりんご、バナナ、オレンジの数を示す棒グラフを作成します。

```python
import matplotlib.pyplot as plt

# 描画するデータ
apples = 10
bananas = 15
oranges = 5

# 棒グラフを作成
plt.bar(["Apples", "Bananas", "Oranges"], [apples, bananas, oranges])

# タイトルを設定
plt.title("Simple Bar Plot")

# x軸のラベルを設定
plt.xlabel("Fruits")

# y軸のラベルを設定
plt.ylabel("Quantity")

# グラフを表示
plt.show()
```
