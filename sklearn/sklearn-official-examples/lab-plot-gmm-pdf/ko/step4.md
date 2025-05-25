# 밀도 추정 플롯

이제 가우시안 혼합 모델의 밀도 추정을 플롯합니다. 데이터셋의 범위에 걸쳐 격자 (meshgrid) 를 생성하고, 각 점에 대한 GMM 이 예측한 음의 로그 - 가능도를 계산합니다. 그런 다음 예측된 점수를 등고선 플롯으로 표시하고, 학습 데이터를 산점도로 표시합니다.

```python
# 모델이 예측한 점수를 등고선 플롯으로 표시
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("가우시안 혼합 모델을 이용한 밀도 추정")
plt.axis("tight")
plt.show()
```
