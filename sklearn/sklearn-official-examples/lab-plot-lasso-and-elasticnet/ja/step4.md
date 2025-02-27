# ElasticNet

ElasticNet は、Lasso 回帰と Ridge 回帰の中間的な手法であり、L1 と L2 のペナルティを組み合わせています。正則化の量は、2 つのハイパーパラメータ `l1_ratio` と `alpha` によって制御されます。`l1_ratio = 0` の場合、ペナルティは純粋な L2 となり、モデルは Ridge 回帰と同等になります。同様に、`l1_ratio = 1` は純粋な L1 ペナルティであり、モデルは Lasso 回帰と同等になります。`0 < l1_ratio < 1` の場合、ペナルティは L1 と L2 の組み合わせになります。

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
