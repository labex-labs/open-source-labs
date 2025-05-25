# 플롯 생성

이 단계에서는 마스크된 배열을 사용하여 서로 다른 단위를 가진 세 개의 플롯을 생성합니다.

```python
# create subplots
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

# plot 1
ax1.scatter(xsecs, xsecs)
ax1.yaxis.set_units(secs)

# plot 2
ax2.scatter(xsecs, xsecs, yunits=hertz)

# plot 3
ax3.scatter(xsecs, xsecs, yunits=minutes)

# set labels
ax1.set_ylabel('Seconds')
ax2.set_ylabel('Hertz')
ax3.set_ylabel('Minutes')
ax3.set_xlabel('Time')
```
