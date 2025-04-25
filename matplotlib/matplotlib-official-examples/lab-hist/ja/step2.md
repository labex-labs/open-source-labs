# ヒストグラムの色を更新する

ヒストグラムメソッドは（他のものとともに）`patches`オブジェクトを返します。これにより、描画されたオブジェクトのプロパティにアクセスできます。これを使って、好みのようにヒストグラムを編集できます。各バーの色をその y 値に基づいて変更してみましょう。

```python
# N は各ビンのカウント、bins はビンの下限
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# 高さで色分けしますが、任意のスカラーを使うこともできます
fracs = N / N.max()

# カラーマップの全範囲に対してデータを 0..1 に正規化する必要があります
norm = colors.Normalize(fracs.min(), fracs.max())

# 次に、オブジェクトをループして、それぞれの色を設定します
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# カウントの合計数で入力を正規化することもできます
axs[1].hist(dist1, bins=n_bins, density=True)

# 次に、y 軸をフォーマットしてパーセンテージを表示します
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```
