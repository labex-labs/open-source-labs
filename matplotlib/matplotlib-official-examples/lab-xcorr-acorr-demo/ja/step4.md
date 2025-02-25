# 自己相関関数のプロット

次に、Matplotlibの`acorr`関数を使って`x`配列の自己相関関数をプロットします。

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

`acorr`関数は以下のパラメータをとります。

- `x`: 自己相関を計算するデータの配列
- `usevlines`: 0から相関値までの垂直線をプロットするかどうかを表すブール値
- `normed`: 相関値を正規化するかどうかを表すブール値
- `maxlags`: 相関を計算する最大のラグ数を表す整数
- `lw`: プロットの線幅を表す整数
