# アニメーションを作成する

次に、`ArtistAnimation` メソッドを使ってアニメーションを作成します。グラフオブジェクト、`ims` リスト、フレーム間のインターバル、および繰り返し遅延を指定します。

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
