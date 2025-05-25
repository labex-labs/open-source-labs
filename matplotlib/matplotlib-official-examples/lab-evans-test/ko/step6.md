# 플롯 생성

이 단계에서는 두 개의 플롯을 생성합니다. 하나는 사용자 정의 단위를 사용하고 다른 하나는 기본 단위를 사용합니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Custom units")
fig.subplots_adjust(bottom=0.2)

# plot specifying units
ax2.plot(x, y, 'o', xunits=2.0)
ax2.set_title("xunits = 2.0")
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')

# plot without specifying units; will use the None branch for axisinfo
ax1.plot(x, y)  # uses default units
ax1.set_title('default units')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

plt.show()
```
