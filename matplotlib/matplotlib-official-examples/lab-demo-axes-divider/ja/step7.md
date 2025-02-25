# プロット

このステップでは、図を作成し、作成したい各画像用のサブプロットを追加します。

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # プロット1
    # シンプルな画像とカラーバー
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # プロット2
    # 描画時の位置指定による画像とカラーバー -- 難しい方法
    demo_locatable_axes_hard(fig)

    # プロット3
    # 描画時の位置指定による画像とカラーバー -- 簡単な方法
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # プロット4
    # 固定パディング付きで横並びの2つの画像。
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```
