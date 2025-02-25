# アニメーションを作成する

`matplotlib.animation`の`FuncAnimation`クラスを使ってアニメーションを作成します。`FuncAnimation`コンストラクタに、グラフオブジェクト、更新関数、フレームの総数（ランダムウォークのステップ数に等しい）、すべてのランダムウォークのリスト、およびすべての線のリストを引数として渡します。

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
