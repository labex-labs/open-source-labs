# 스파인 위치 조정 메서드 정의

이 단계에서는 지정된 스파인 위치를 기반으로 축 스파인의 위치를 조정하는 메서드를 정의합니다.

```python
def adjust_spines(ax, spines):
    """
    지정된 스파인 위치를 기반으로 축 스파인의 위치를 조정합니다.

    Parameters:
        ax (Axes): 스파인을 조정할 Matplotlib Axes 객체입니다.
        spines (list of str): 원하는 스파인 위치입니다. 유효한 옵션은 'left', 'right', 'top', 'bottom'입니다.

    Returns:
        None
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # move the spine outward by 10 points
        else:
            spine.set_color('none')  # don't draw the spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
