# 수평 및 수직선 추가

이제, 속성 순환 (property cycle) 의 색상을 사용하여 각 서브플롯에 수평 및 수직선을 추가합니다.

```python
for icol in range(2):
    if icol == 0:
        lwx, lwy = thin, lwbase
    else:
        lwx, lwy = lwbase, thick
    for irow in range(2):
        for i, color in enumerate(colors):
            axs[irow, icol].axhline(i, color=color, lw=lwx)
            axs[irow, icol].axvline(i, color=color, lw=lwy)
```
