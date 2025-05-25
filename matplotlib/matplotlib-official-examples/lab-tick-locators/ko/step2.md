# 플롯 설정

다음으로, figure 와 서브플롯 (subplot) 배열을 생성하여 플롯을 설정합니다. 또한 예제에서 축에 대한 공통 매개변수를 설정하는 `setup` 함수를 정의합니다.

```python
fig, axs = plt.subplots(8, 1, figsize=(8, 6))

def setup(ax, title):
    """예제에서 Axes 에 대한 공통 매개변수를 설정합니다."""
    # 하단 스파인만 표시
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')
```
