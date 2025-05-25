# 모델 학습

데이터를 분류하기 위해 GPC 모델을 사용할 것입니다. 먼저 커널 함수를 지정해야 합니다.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

그런 다음 GPC 모델을 생성하고 데이터를 사용하여 학습시킬 수 있습니다.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
