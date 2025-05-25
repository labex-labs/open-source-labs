# 커널 릿지 회귀 모델 적합

이제 데이터에 커널 릿지 회귀 모델을 적합합니다. 비선형 회귀에 일반적으로 사용되는 RBF(Radial Basis Function) 커널을 사용합니다.

```python
# 커널 릿지 회귀 모델 적합
alpha = 1.0  # 정규화 매개변수
gamma = 0.1  # RBF 커널의 커널 계수
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
