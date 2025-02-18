# プロットの設定

新しいグラフウィンドウ（figure）と軸オブジェクト（axis）を作成し、Scope クラスを初期化します。次に、更新関数（update）とエミッター関数（emitter）を FuncAnimation メソッドに渡してアニメーションを作成します。

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
