# 히스토그램 사용자 정의

`color`, `alpha`, 그리고 `edgecolor` 매개변수를 사용하여 막대의 색상, 투명도 및 테두리 색상을 변경하여 히스토그램을 사용자 정의할 수 있습니다.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
