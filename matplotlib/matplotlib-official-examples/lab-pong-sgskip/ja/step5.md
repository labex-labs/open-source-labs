# ゲームアニメーションを作成する

`Game` クラスを定義したので、`Game` オブジェクトをインスタンス化し、ループ内でその `draw()` メソッドを呼び出すことで、ゲームアニメーションを作成できます。

```python
fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = Game(ax)

# デフォルトのキーバインドを無効にする
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# 再描画時にブリッティング背景をリセットする
def on_redraw(event):
    animation.background = None


# 最初の描画後に起動する
def start_anim(event):
    canvas.mpl_disconnect(start_anim.cid)

    start_anim.timer.add_callback(animation.draw)
    start_anim.timer.start()
    canvas.mpl_connect('draw_event', on_redraw)


start_anim.cid = canvas.mpl_connect('draw_event', start_anim)
start_anim.timer = animation.canvas.new_timer(interval=1)

tstart = time.time()

plt.show()
print('FPS: %f' % (animation.cnt/(time.time() - tstart)))
```
