# 전처리 파이프라인에 분류기를 추가

이 단계에서는 `Pipeline`을 사용하여 로지스틱 회귀 분류기를 전처리 파이프라인에 추가합니다.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
