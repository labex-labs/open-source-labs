# 높은 농도 사전을 사용한 베이지안 GMM 결과 시각화

이제 디리클레 과정 사전과 높은 농도 사전을 사용한 베이지안 가우시안 혼합 모델의 결과를 시각화합니다.

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    2,
    "디리클레 과정 사전을 사용한 베이지안 가우시안 혼합 모델 "
    r"($\gamma_0=100$) 의 결과"
)
```
