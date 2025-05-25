# 내부 GridSpec 에 서브플롯 추가

이제 내부 gridspec 에 서브플롯을 추가합니다. `ax1`, `ax2`, 그리고 `ax3` 세 개의 서브플롯을 생성합니다.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
