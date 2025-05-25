# 스택 히스토그램 플롯

`stacked` 매개변수를 `True`로 설정하여 스택 히스토그램을 플롯할 수 있습니다.

```python
plt.hist(x, n_bins, color=['green', 'blue', 'red'], alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'], stacked=True)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Random Data')
plt.legend()
plt.show()
```
