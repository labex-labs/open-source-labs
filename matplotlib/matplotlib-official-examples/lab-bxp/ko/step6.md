# 다양한 요소의 표시 사용자 정의

`bxp()` 함수의 다양한 매개변수를 사용하여 상자 그림의 다양한 요소 표시를 사용자 정의할 수 있습니다. 이 예제에서는 상자, 중앙값, 이상치 (fliers), 평균 점, 평균 선을 사용자 정의하는 방법을 보여줍니다.

```python
# Customize the display of different elements
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12, linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

plt.bxp(stats, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, meanline=True, showmeans=True)
plt.show()
```
