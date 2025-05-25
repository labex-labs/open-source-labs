# GridSpec 에 서브플롯 추가

`fig.add_subplot()` 함수를 사용하여 GridSpec 에 서브플롯을 추가할 수 있습니다. GridSpec 객체의 인덱싱 표기법을 사용하여 그리드 내 서브플롯의 위치를 지정할 수 있습니다. 예를 들어, `gs[0, :]`는 첫 번째 행과 모든 열을 지정합니다.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
