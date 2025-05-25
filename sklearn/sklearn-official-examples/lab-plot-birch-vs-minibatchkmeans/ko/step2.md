# Blob 생성

다음 단계는 MiniBatchKMeans 와 BIRCH 간의 비교를 위해 Blob 을 생성하는 것입니다. matplotlib 에서 기본적으로 제공하는 모든 색상을 사용할 것입니다.

```python
# Blob 의 중심을 생성하여 10 x 10 그리드를 형성합니다.
xx = np.linspace(-22, 22, 10)
yy = np.linspace(-22, 22, 10)
xx, yy = np.meshgrid(xx, yy)
n_centers = np.hstack((np.ravel(xx)[:, np.newaxis], np.ravel(yy)[:, np.newaxis]))

# MiniBatchKMeans 와 BIRCH 간의 비교를 위해 Blob 을 생성합니다.
X, y = make_blobs(n_samples=25000, centers=n_centers, random_state=0)

# matplotlib 에서 기본적으로 제공하는 모든 색상을 사용합니다.
colors_ = cycle(colors.cnames.keys())
```
