# 축 공유 (Sharing Axes)

기본적으로 각 `Axes`는 개별적으로 스케일링됩니다. 서브플롯의 수평 또는 수직 축을 정렬하려면, `sharex` 또는 `sharey` 매개변수를 사용할 수 있습니다.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
