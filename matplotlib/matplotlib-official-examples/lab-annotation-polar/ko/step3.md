# 주석 추가

극좌표 그래프에 주석을 추가하려면 주석의 위치를 지정해야 합니다. 이 경우, 그래프의 특정 지점을 선택하고 주석을 추가합니다.

```python
ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
```
