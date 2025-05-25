# 여러 좌표계 및 축 유형 사용

`xypoint`와 `xytext`를 서로 다른 위치와 좌표계로 지정할 수 있으며, 선택적으로 연결선 (connecting line) 을 켜고 마커로 점을 표시할 수 있습니다. 주석은 극좌표 축 (polar axes) 에서도 작동합니다.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(3, 3))
r = np.arange(0, 1, 0.001)
theta = 2*2*np.pi*r
line, = ax.plot(theta, r)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom')
```
