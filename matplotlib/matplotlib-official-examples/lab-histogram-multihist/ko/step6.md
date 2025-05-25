# 여러 히스토그램 플롯

`hist` 함수에 데이터 배열을 전달하여 동일한 플롯에 여러 히스토그램을 플롯할 수 있습니다.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```
