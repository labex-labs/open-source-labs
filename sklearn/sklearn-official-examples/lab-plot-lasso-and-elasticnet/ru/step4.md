# ElasticNet

ElasticNet представляет собой компромисс между Lasso и Ridge-регрессией, так как комбинирует L1- и L2-штрафы. Величина регуляризации контролируется двумя гиперпараметрами `l1_ratio` и `alpha`. При `l1_ratio = 0` штраф является чисто L2, и модель эквивалентна Ridge-регрессии. Аналогично, `l1_ratio = 1` представляет собой чисто L1-штраф, и модель эквивалентна Lasso-регрессии. При `0 < l1_ratio < 1` штраф является комбинацией L1 и L2.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
