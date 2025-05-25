# y 축 눈금 사용자 정의

가장 왼쪽 서브플롯의 y 축 눈금을 사용자 정의합니다.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
