# アニメーションを作成する

アニメーションの各フレームを反復処理するために for ループを使用します。各反復処理では、軸をクリアし、現在のフレームを描画し、タイトルを設定し、アニメーションが表示されるように短い時間だけ一時停止します。

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
