# 임베딩 변환기 학습

`RandomTreesEmbedding`은 비지도 학습 방법으로 별도로 학습할 필요가 없습니다.

```python
from sklearn.ensemble import RandomTreesEmbedding

random_tree_embedding = RandomTreesEmbedding(
    n_estimators=n_estimators, max_depth=max_depth, random_state=0
)

rt_model = make_pipeline(random_tree_embedding, LogisticRegression(max_iter=1000))
rt_model.fit(X_train_linear, y_train_linear)
```
