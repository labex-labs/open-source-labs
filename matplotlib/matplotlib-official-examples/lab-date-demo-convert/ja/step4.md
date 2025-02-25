# グラフを作成する

これで、日付とy値を使ってグラフを作成できます。まず、subplots関数を使ってfigureとaxisオブジェクトを作成します。そして、plot関数を使ってグラフを描画します。次のコードをコピーして貼り付けます。

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
