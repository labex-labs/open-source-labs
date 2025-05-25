# 박스 플롯 스타일 사용자 정의

`boxplot()` 함수에서 사용할 수 있는 다양한 키워드 인수를 사용하여 박스 플롯의 스타일을 사용자 정의할 수도 있습니다. 예를 들어, `boxprops`를 설정하여 박스의 색상과 선 스타일을 변경할 수 있습니다. 또한 `medianprops`, `meanprops`, `meanlineprops`를 각각 설정하여 중앙값 (median), 평균 (mean), 평균선 (mean line) 의 스타일을 변경할 수 있습니다.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

boxprops = dict(linestyle='--', linewidth=2, color='red')
axs[0, 1].boxplot(data, labels=labels, boxprops=boxprops)
axs[0, 1].set_title('Custom Box')

medianprops = dict(linestyle='-', linewidth=2, color='blue')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')
meanlineprops = dict(linestyle='--', linewidth=2, color='red')
axs[1, 0].boxplot(data, labels=labels, medianprops=medianprops, meanprops=meanprops, meanline=True, meanlineprops=meanlineprops)
axs[1, 0].set_title('Custom Median, Mean, and Mean Line')

flierprops = dict(marker='o', markerfacecolor='red', markersize=8, markeredgecolor='none')
axs[1, 1].boxplot(data, labels=labels, flierprops=flierprops)
axs[1, 1].set_title('Custom Outliers')

plt.show()
```
