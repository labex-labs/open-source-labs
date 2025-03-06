# ライブラリのセットアップとサンプルデータの作成

最初のステップでは、必要なライブラリをインポートし、プロット用のサンプル金融データを作成します。可視化には Matplotlib を、データ生成には NumPy をインポートする必要があります。

ノートブックの最初のセルに、以下のコードを入力して実行し、必要なライブラリをインポートします。

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

コードを実行した後（Shift+Enter を押す）、以下の出力が表示されるはずです。

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

次に、可視化するためのサンプル金融データを作成しましょう。金融データは多くの場合、時間の経過に伴う値を表すため、ある期間の日次収益を表す簡単なデータセットを作成します。

新しいセルに以下のコードを追加して実行します。

```python
# Set a random seed for reproducibility
np.random.seed(42)

# Generate financial data: 30 days of revenue data
days = np.arange(1, 31)
daily_revenue = np.random.uniform(low=1000, high=5000, size=30)

print("Sample of daily revenue data (first 5 days):")
for i in range(5):
    print(f"Day {days[i]}: ${daily_revenue[i]:.2f}")
```

このコードを実行すると、サンプル収益データの最初の 5 日分が表示されます。

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

このサンプルデータは、30 日間の日次収益が 1,000 ドルから 5,000 ドルの間の値を表しています。次のステップでこのデータを使ってプロットを作成します。
