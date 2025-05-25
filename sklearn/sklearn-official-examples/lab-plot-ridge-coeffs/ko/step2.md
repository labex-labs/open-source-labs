# 랜덤 데이터 생성

scikit-learn 의 `make_regression` 함수를 사용하여 랜덤 데이터를 생성합니다. `n_samples`를 10, `n_features`를 10, `random_state`를 1 로 설정합니다. 이 함수는 입력 특징 X, 목표 변수 y, 그리고 실제 계수 값 w 를 반환합니다.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
