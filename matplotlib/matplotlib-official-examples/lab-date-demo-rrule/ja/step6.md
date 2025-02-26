# データをプロットしてx軸の目盛りを設定する

最後に、plot関数を使ってデータをプロットし、先ほど設定した目盛りの位置付け関数と書式設定関数を使ってx軸の目盛りを設定することができます。

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```