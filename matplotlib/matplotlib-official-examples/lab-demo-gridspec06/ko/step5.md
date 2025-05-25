# 외부 스파인만 표시

이 단계에서는 내부 서브플롯의 스파인을 제거하고 외부 스파인만 표시합니다. 이렇게 하면 플롯이 더 깔끔하게 보입니다.

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
