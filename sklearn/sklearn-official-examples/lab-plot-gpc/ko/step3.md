# 모델 학습

고정 및 최적화된 하이퍼파라미터를 사용하여 GPC 모델을 학습합니다. 모델의 로그 - 주변 - 가능도, 정확도 및 로그 손실을 출력합니다.

```python
# 고정된 하이퍼파라미터
gp_fix = GaussianProcessClassifier(kernel=1.0 * RBF(length_scale=1.0), optimizer=None)
gp_fix.fit(X[:train_size], y[:train_size])

# 최적화된 하이퍼파라미터
gp_opt = GaussianProcessClassifier(kernel=1.0 * RBF(length_scale=1.0))
gp_opt.fit(X[:train_size], y[:train_size])

# 결과
print("로그 주변 가능도 (초기): %.3f" % gp_fix.log_marginal_likelihood(gp_fix.kernel_.theta))
print("로그 주변 가능도 (최적화): %.3f" % gp_opt.log_marginal_likelihood(gp_opt.kernel_.theta))
print("정확도: %.3f (초기) %.3f (최적화)" % (accuracy_score(y[:train_size], gp_fix.predict(X[:train_size])), accuracy_score(y[:train_size], gp_opt.predict(X[:train_size]))))
print("로그 손실: %.3f (초기) %.3f (최적화)" % (log_loss(y[:train_size], gp_fix.predict_proba(X[:train_size])[:, 1]), log_loss(y[:train_size], gp_opt.predict_proba(X[:train_size])[:, 1])))
```
