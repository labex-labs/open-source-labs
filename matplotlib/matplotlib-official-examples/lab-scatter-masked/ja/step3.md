# データポイントのマスクと散布図の作成

原点からの距離に基づいてデータポイントをマスクします。距離が`r0`未満のデータポイントは`area1`でマスクされ、距離が`r0`以上のデータポイントは`area2`でマスクされます。その後、`area1`と`area2`に対してそれぞれ`marker='^'`と`marker='o'`を使って、マスクされたデータポイントの散布図を作成します。

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
