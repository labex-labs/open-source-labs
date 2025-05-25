# Figure 및 Subplot 생성

두 번째 단계는 애니메이션에 사용될 figure 와 subplot 을 생성하는 것입니다. 이 예제에서는 서로 다른 종횡비 (aspect ratio) 를 가진 두 개의 subplot 을 나란히 생성합니다. 왼쪽 subplot 은 단위 원이고, 오른쪽 subplot 은 사인 곡선을 애니메이션하는 데 사용될 빈 플롯입니다.

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
