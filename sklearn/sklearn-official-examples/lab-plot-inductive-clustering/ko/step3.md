# 새로운 샘플 생성

이 단계에서는 새로운 샘플을 생성하고 원본 데이터셋과 함께 플롯합니다. `make_blobs` 함수를 다시 사용하여 10 개의 새로운 샘플을 생성합니다.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```
