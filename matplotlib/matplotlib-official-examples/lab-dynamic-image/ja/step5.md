# アニメーションフレームを作成する

次に、アニメーション用のフレームを作成します。60 フレームを生成するために for ループを使用します。ループの各反復では、x と y のデータを更新し、その後 `imshow` メソッドを使って新しい画像オブジェクトを作成します。そして、画像オブジェクトを `ims` リストに追加します。

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```
