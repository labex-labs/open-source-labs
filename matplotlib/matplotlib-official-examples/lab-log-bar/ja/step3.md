# 棒グラフの作成

これで、棒グラフを作成する準備が整いました。まず、棒の幅と x 軸上の位置を設定するのに役立ついくつかの変数を定義します。

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

次に、`subplots()` メソッドを使ってグラフと軸のオブジェクトを作成します。そして、for ループを使ってデータセットの各値を反復処理し、それぞれに対して棒を作成します。

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

対数スケールと互換性のない高さ 0 の棒がないように、`bottom` パラメータを `0.001` に設定します。
