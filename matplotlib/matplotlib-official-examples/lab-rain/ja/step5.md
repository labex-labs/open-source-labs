# アニメーションを作成する

最後に、FuncAnimation オブジェクトを使用してアニメーションを作成します。ここでは、グラフ、更新関数、フレーム間の間隔（ミリ秒）、および保存するフレーム数を指定します。

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
