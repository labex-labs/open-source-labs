# 데이터셋 생성

이 단계에서는 `sklearn.datasets`의 `make_multilabel_classification` 함수를 사용하여 데이터셋을 생성합니다.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
