# 데이터 및 히스토그램 생성

NumPy 를 사용하여 데이터와 히스토그램을 생성합니다.

```python
# histogram our data with numpy
data = np.random.randn(1000)
n, _, _ = plt.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
```
