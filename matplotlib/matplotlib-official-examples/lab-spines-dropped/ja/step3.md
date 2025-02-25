# グラフと軸の作成

`plt.subplots()` を使ってグラフと軸のオブジェクトを作成します。`imshow()` 関数を使って、ランダムなデータを画像として表示します。

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
