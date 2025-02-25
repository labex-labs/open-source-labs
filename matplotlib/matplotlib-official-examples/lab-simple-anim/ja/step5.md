# アニメーションオブジェクトの作成

ここでは、`FuncAnimation()`関数を使ってアニメーションオブジェクトを作成できます。グラフオブジェクト、アニメーション関数、更新間隔、保存するフレーム数を渡します。

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
