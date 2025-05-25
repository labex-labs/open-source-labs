# 최근접 이웃 그래프 캐싱

이 단계에서는 파이프라인의 캐싱 기능을 사용하여 KNeighborsClassifier 의 여러 적합 과정에서 최근접 이웃 그래프를 캐싱합니다.

```python
# 하이퍼파라미터 튜닝 시 여러 번 사용될 그래프 계산 결과를 캐싱하기 위해 `memory` 에 디렉토리를 지정합니다.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
