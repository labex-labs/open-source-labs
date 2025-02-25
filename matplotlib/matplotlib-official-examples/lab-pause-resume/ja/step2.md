# アニメーションの定義

このステップでは、作成したいアニメーションを定義します。各フレームで右に移動する正規分布を表示するアニメーションを作成します。

```python
class PauseAnimation:
    def __init__(self):
        # グラフと軸を作成
        fig, ax = plt.subplots()
        ax.set_title('Click to pause/resume the animation')

        # x軸の値を作成
        x = np.linspace(-0.1, 0.1, 1000)

        # 正規分布から始める
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # プロットを作成
        self.p, = ax.plot(x, self.n0)

        # アニメーションを作成
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # アニメーションを一時停止状態に設定
        self.paused = False

        # 一時停止を切り替えるためのボタン押下イベントを追加
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # 一時停止と再開を切り替える
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # 正規分布を更新
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
