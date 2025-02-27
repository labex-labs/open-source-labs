# データをプロットし、x 軸の目盛りを設定する

最後に、`plot` 関数を使用してデータをプロットし、前に設定した目盛りの配置器 (tick locator) と書式設定器 (formatter) 関数を使用して x 軸の目盛りを設定できます。

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
