# アニメーションを作成する

これで `UpdateDist` クラスを定義したので、Matplotlib の `FuncAnimation` クラスを使ってアニメーションを作成できます。グラフオブジェクトと軸オブジェクトを作成し、軸オブジェクトを `UpdateDist` クラスに渡して、そのクラスの新しいインスタンスを作成します。

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

`FuncAnimation` クラスはいくつかの引数を取ります。

- `fig`：グラフオブジェクト
- `ud`：`UpdateDist` インスタンス
- `frames`：アニメーションするフレーム数
- `interval`：フレーム間の時間（ミリ秒）
- `blit`：変更された部分のみを更新するかどうか
