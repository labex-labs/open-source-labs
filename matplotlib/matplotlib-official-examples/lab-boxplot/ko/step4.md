# 개별 구성 요소 제거

`boxplot()` 함수에서 사용할 수 있는 다양한 키워드 인수를 사용하여 박스 플롯의 개별 구성 요소를 제거할 수 있습니다. 예를 들어, `showmeans`를 False 로 설정하여 평균을 제거할 수 있습니다. 또한 `showbox`와 `showcaps`를 각각 False 로 설정하여 박스와 수염 (whiskers) 을 제거할 수도 있습니다.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```
