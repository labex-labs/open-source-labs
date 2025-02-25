# アニメーションの作成

7 番目のステップは、`FuncAnimation` 関数を使ってアニメーションオブジェクトを作成することです。グラフオブジェクト、アニメーション関数、フレーム間のインターバル（ミリ秒）、フレーム数、そしてアニメーションを繰り返す前の遅延を渡します。

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
```
