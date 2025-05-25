# 기본 바이올린 플롯 생성

다음으로, Matplotlib 의 `violinplot` 함수를 사용하여 기본 바이올린 플롯을 생성합니다. 이는 이후 단계에서 플롯을 사용자 정의할 때 비교를 위한 기준선을 제공합니다.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
