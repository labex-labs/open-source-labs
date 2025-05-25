# Figure 1 변경

이제 첫 번째 figure 로 다시 전환하여 몇 가지 변경을 수행합니다. 두 번째 사인파를 상단 subplot 에 사각형 마커를 사용하여 플롯하고, 상단 subplot 에서 x 축 눈금 레이블을 제거합니다.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])
```
