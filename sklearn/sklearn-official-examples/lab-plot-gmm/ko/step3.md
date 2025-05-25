# 가우시안 혼합 모델 구현

이 단계에서는 scikit-learn 의 `GaussianMixture` 클래스를 사용하여 가우시안 혼합 모델을 구현합니다. 모델을 데이터셋에 맞추고 각 데이터 포인트의 클러스터 레이블을 예측합니다. 마지막으로 결과를 시각화합니다.

```python
# 5 개의 구성 요소를 가진 GMM 객체 생성
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# 데이터에 GMM 적합
gmm.fit(X)

# 클러스터 레이블 예측
Y_ = gmm.predict(X)

# 결과 시각화
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="클러스터 {}".format(i)
    )

plt.legend(loc="best")
plt.title("가우시안 혼합 모델")
plt.show()
```
