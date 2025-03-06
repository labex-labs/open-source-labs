# 環境の準備とデータの作成

最初のステップでは、必要なライブラリをインポートして作業環境をセットアップし、可視化用のサンプルデータを作成します。外れ値（アウトライヤー）を含むデータを生成し、破線軸グラフ（ブロークンアクシスプロット）の有用性を実証します。

## 必要なライブラリのインポート

まず、このチュートリアルで必要なライブラリをインポートしましょう。可視化には Matplotlib を、数値データの生成と操作には NumPy を使用します。

Jupyter Notebook で新しいセルを作成し、以下のコードを入力します。

```python
import matplotlib.pyplot as plt
import numpy as np

print(f"NumPy version: {np.__version__}")
```

このセルを実行すると、以下のような出力が表示されるはずです。

```
NumPy version: 2.0.0
```

![numpy-version](../assets/screenshot-20250306-Um0MaTKw@2x.png)

正確なバージョン番号は環境によって異なる場合がありますが、これによりライブラリが正しくインストールされ、使用可能であることが確認できます。

## 外れ値を含むサンプルデータの生成

次に、外れ値を含むサンプルデータセットを作成しましょう。乱数を生成し、特定の位置に大きな値を意図的に追加して外れ値を作成します。

新しいセルを作成し、以下のコードを追加します。

```python
# Set random seed for reproducibility
np.random.seed(19680801)

# Generate 30 random points with values between 0 and 0.2
pts = np.random.rand(30) * 0.2

# Add 0.8 to two specific points to create outliers
pts[[3, 14]] += 0.8

# Display the first few data points to understand our dataset
print("First 10 data points:")
print(pts[:10])
print("\nData points containing outliers:")
print(pts[[3, 14]])
```

このセルを実行すると、以下のような出力が表示されるはずです。

```
First 10 data points:
[0.01182225 0.11765474 0.07404329 0.91088185 0.10502995 0.11190702
 0.14047499 0.01060192 0.15226977 0.06145634]

Data points containing outliers:
[0.91088185 0.97360754]
```

この出力から、インデックス 3 と 14 の値が他の値よりもはるかに大きいことが明らかです。これらが外れ値です。ほとんどのデータポイントは 0.2 未満ですが、この 2 つの外れ値は 0.9 を超えており、データセットに大きな差異が生じています。

このようなデータ分布は、破線軸グラフの有用性を実証するのに最適です。次のステップでは、グラフの構造を作成し、メインデータと外れ値の両方を適切に表示するように設定します。
