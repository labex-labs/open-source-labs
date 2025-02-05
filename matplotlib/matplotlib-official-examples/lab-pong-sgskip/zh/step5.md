# 创建游戏动画

既然我们已经定义了 `Game` 类，那么我们可以通过实例化一个 `Game` 对象并在循环中调用它的 `draw()` 方法来创建游戏动画。

```python
fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = Game(ax)

# 禁用默认的按键绑定
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# 在重绘时重置位图背景
def on_redraw(event):
    animation.background = None


# 在第一次绘制后启动动画
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
