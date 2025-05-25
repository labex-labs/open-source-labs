# 히스토그램 생성

이 단계에서는 matplotlib 을 사용하여 히스토그램을 생성합니다. 빈 (bin) 의 수를 50 으로 설정하고, 히스토그램의 적분이 1 이 되도록 빈 높이를 정규화하기 위해 density 매개변수를 활성화합니다.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
