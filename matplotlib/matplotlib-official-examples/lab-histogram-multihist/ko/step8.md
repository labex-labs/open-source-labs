# 스텝 히스토그램 플롯

`histtype` 매개변수를 `'step'`으로 설정하여 스텝 히스토그램을 플롯할 수 있습니다.

```python
plt.hist(x, n_bins, histtype='step', color=['green', 'blue', 'red'], label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Step Histogram of Random Data')
plt.legend()
plt.show()
```
