# ElasticNet

ElasticNet est un compromis entre la régression Lasso et la régression Ridge, car elle combine une pénalité L1 et une pénalité L2. Le degré de régularisation est contrôlé par les deux hyperparamètres `l1_ratio` et `alpha`. Pour `l1_ratio = 0`, la pénalité est purement L2 et le modèle est équivalent à une régression Ridge. De même, `l1_ratio = 1` est une pénalité pure L1 et le modèle est équivalent à une régression Lasso. Pour `0 < l1_ratio < 1`, la pénalité est une combinaison de L1 et L2.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
