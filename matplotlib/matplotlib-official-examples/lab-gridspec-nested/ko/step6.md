# 두 번째 내부 GridSpec 에 서브플롯 추가

이제 두 번째 내부 gridspec 에 서브플롯을 추가합니다. `ax4`, `ax5`, 그리고 `ax6` 세 개의 서브플롯을 생성합니다.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
