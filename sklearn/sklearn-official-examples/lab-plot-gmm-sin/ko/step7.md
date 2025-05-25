# 낮은 농도 사전을 사용한 베이지안 GMM 에서 샘플링

이제 디리클레 과정 사전과 낮은 농도 사전을 사용한 베이지안 가우시안 혼합 모델에서 샘플링합니다.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    0,
    "디리클레 과정 사전을 사용한 가우시안 혼합 모델 "
    r"($\gamma_0=0.01$) 에서 2000 개의 샘플로 샘플링한 결과."
)
```
