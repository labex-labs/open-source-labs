# 그룹화된 막대 차트 생성

이제 Matplotlib 의 `bar` 함수를 사용하여 차트를 생성할 수 있습니다. 속성을 반복하고 각 속성에 대한 막대 세트를 생성하는 루프를 만들 것입니다. 또한 막대의 너비와 각 막대 세트의 위치를 조정합니다.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
