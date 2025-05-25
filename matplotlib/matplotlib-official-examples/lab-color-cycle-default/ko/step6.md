# 서브플롯 사용자 정의

아래쪽 서브플롯의 배경색을 검정색으로 설정하고, x 축 눈금을 설정하며, 각 서브플롯에 제목을 추가하여 서브플롯을 사용자 정의합니다.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
