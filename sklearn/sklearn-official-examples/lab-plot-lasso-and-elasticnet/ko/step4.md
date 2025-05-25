# ElasticNet

ElasticNet 은 Lasso 와 Ridge 회귀 사이의 중간 지점으로 L1 및 L2 페널티를 결합합니다. 정규화의 양은 두 하이퍼파라미터 `l1_ratio`와 `alpha`로 제어됩니다. `l1_ratio = 0`인 경우 페널티는 순수한 L2 이며 모델은 Ridge 회귀와 동일합니다. 마찬가지로 `l1_ratio = 1`은 순수한 L1 페널티이며 모델은 Lasso 회귀와 동일합니다. `0 < l1_ratio < 1`인 경우 페널티는 L1 과 L2 의 조합입니다.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
