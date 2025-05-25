# 사용자 정의 빈 너비 (bin width) 를 가진 히스토그램 생성

빈 경계 (bin edge) 목록을 제공하여 사용자 정의 및 불균등한 빈 너비 (bin width) 를 가진 히스토그램을 생성할 수 있습니다. 이 예제에서는 불균등하게 간격이 떨어진 빈 (bin) 을 가진 히스토그램을 생성합니다.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
