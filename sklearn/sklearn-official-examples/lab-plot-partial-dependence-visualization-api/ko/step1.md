# 당뇨병 데이터셋으로 모델 학습

이 단계에서는 당뇨병 데이터셋으로 의사 결정 트리와 다층 퍼셉트론을 학습합니다.

```python
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target

tree = DecisionTreeRegressor()
mlp = make_pipeline(
    StandardScaler(),
    MLPRegressor(hidden_layer_sizes=(100, 100), tol=1e-2, max_iter=500, random_state=0),
)
tree.fit(X, y)
mlp.fit(X, y)
```
