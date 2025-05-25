# 데이터 클러스터링

모델이 적합된 후에는 각 샘플을 속한 가우시안 구성 요소에 할당하여 데이터를 클러스터링할 수 있습니다. `GaussianMixture` 클래스의 `predict` 메서드를 이 목적으로 사용할 수 있습니다.

```python
# 데이터 클러스터링
cluster_labels = gmm.predict(X_test)
```
