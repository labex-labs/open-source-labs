# 마스킹된 영역을 구분하는 선 추가

마지막으로, 마스킹된 영역을 구분하기 위해 선을 추가합니다. 세타 (theta) 값의 배열을 생성하고 `np.cos(theta)`와 `np.sin(theta)`를 사용하여 반지름이 `r0`인 원을 플롯합니다.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
