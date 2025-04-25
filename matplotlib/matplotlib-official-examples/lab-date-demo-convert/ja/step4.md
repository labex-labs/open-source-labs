# グラフを作成する

これで、日付と y 値を使ってグラフを作成できます。まず、subplots 関数を使って figure と axis オブジェクトを作成します。そして、plot 関数を使ってグラフを描画します。次のコードをコピーして貼り付けます。

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
