# グラフのカスタマイズ

Matplotlib は、グラフに対して幅広いカスタマイズオプションを提供しています。以下は、単純な線グラフをカスタマイズするコード例です。

```python
import matplotlib.pyplot as plt

# データ
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# グラフを作成する
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# ラベルとタイトルを追加する
plt.xlabel('X 軸')
plt.ylabel('Y 軸')
plt.title('カスタマイズされたグラフ')

# グラフを表示する
plt.show()
```

このコードでは、`plot()` メソッドのさまざまなパラメータを使用してグラフをカスタマイズしています。線の色を赤色に、線幅を 2 に、線のスタイルを破線 (`--`) に、マーカーを丸 (`o`) に、マーカーサイズを 8 に、マーカーの塗りつぶし色を黄色に変更しています。
