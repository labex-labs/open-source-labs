# グラフのフォーマット設定

次に、x軸とy軸のラベルを追加し、x軸の主目盛り位置とフォーマッタを設定し、y軸とスパインを削除することでグラフのフォーマットを設定します。以下はグラフのフォーマット設定のコードです。

```python
# 4ヶ月間隔でx軸をフォーマットする
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# y軸とスパインを削除する
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
```
