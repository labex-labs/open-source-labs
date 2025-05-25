# 데이터 로드 및 파이프라인 정의

scikit-learn 에서 숫자 데이터셋을 로드하고 PCA 와 LinearSVC 로 구성된 파이프라인을 정의합니다.

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
