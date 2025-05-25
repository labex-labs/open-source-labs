# 히스토그램 스타일 변경

`hist` 함수에서 `histtype` 매개변수를 지정하여 히스토그램의 스타일을 변경할 수 있습니다. 이 예제에서는 색상 채우기가 있는 스텝 곡선 (step curve) 을 가진 히스토그램을 생성합니다.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
