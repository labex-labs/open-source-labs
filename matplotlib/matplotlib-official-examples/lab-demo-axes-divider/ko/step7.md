# 플로팅 (Plotting)

이 단계에서는 그림을 생성하고 생성하려는 각 이미지에 대한 서브플롯을 추가합니다.

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # PLOT 1
    # simple image & colorbar
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # PLOT 2
    # image and colorbar with draw-time positioning -- a hard way
    demo_locatable_axes_hard(fig)

    # PLOT 3
    # image and colorbar with draw-time positioning -- an easy way
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # PLOT 4
    # two images side by side with fixed padding.
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```
