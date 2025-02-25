# 相関関数のプロット

次に、Matplotlibの`xcorr`関数を使って2つの配列間の相関関数をプロットします。

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

`xcorr`関数は以下のパラメータをとります。

- `x`: 最初のデータ配列
- `y`: 2番目のデータ配列
- `usevlines`: 0から相関値までの垂直線をプロットするかどうかを表すブール値
- `maxlags`: 相関を計算する最大のラグ数を表す整数
- `normed`: 相関値を正規化するかどうかを表すブール値
- `lw`: プロットの線幅を表す整数
