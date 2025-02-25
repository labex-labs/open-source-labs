# 円グラフの作成

Matplotlib を使って円グラフを作成することもできます。この例では、異なる種類のピザを好む人の割合を示す円グラフを作成します。

```python
import matplotlib.pyplot as plt

# 描画するデータ
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Mushroom", "Onion", "Sausage"]

# 円グラフを作成
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# タイトルを設定
plt.title("Simple Pie Chart")

# グラフを表示
plt.show()
```
