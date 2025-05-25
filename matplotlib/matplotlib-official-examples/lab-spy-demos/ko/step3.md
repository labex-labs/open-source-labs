# 서브플롯 생성

이제 `subplots` 함수를 사용하여 2x2 그리드의 서브플롯을 생성합니다. 이를 통해 배열의 희소 패턴을 시각화할 네 개의 플롯을 얻을 수 있습니다.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```
