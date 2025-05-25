# 계수를 통한 특징 중요도

특징의 중요도를 파악하기 위해 RidgeCV 추정기를 사용합니다. 절댓값이 가장 큰 `coef_` 값을 가진 특징이 가장 중요하다고 간주합니다.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("계수를 통한 특징 중요도")
plt.show()
```
