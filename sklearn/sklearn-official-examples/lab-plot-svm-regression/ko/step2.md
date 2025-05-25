# 회귀 모델 적합

다음으로, 선형, 다항식 및 RBF 커널을 사용하여 샘플 데이터 세트에 SVR 모델을 적합시킵니다. 각 모델의 하이퍼파라미터를 설정하고 샘플 데이터 세트에서 학습시킵니다.

```python
from sklearn.svm import SVR

# 회귀 모델 적합
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
