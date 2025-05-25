# 이상치가 포함된 데이터 생성

100 개의 내부 데이터 포인트와 20 개의 이상치 데이터 포인트를 가진 120 개의 데이터 포인트로 구성된 데이터 세트를 생성합니다. 그런 다음 데이터를 플롯하여 이상치를 시각화합니다.

```python
np.random.seed(42)

X_inliers = 0.3 * np.random.randn(100, 2)
X_inliers = np.r_[X_inliers + 2, X_inliers - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X = np.r_[X_inliers, X_outliers]

plt.scatter(X[:, 0], X[:, 1], color="k", s=3.0)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("데이터 포인트")
plt.title("이상치가 포함된 데이터")
plt.show()
```
