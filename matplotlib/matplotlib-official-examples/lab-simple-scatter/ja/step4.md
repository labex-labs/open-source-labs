# アニメーションの作成

最後のステップは、アニメーションを作成することです。これは、animation モジュールの FuncAnimation 関数を使用して行います。この関数には、グラフオブジェクト、グラフを更新する関数、および使用するフレーム数など、いくつかの引数が必要です。

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
