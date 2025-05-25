# 데이터셋 로드

이 단계에서는 Scikit-Learn 의 `make_hastie_10_2` 함수를 사용하여 데이터셋을 로드합니다. 이 함수는 이진 분류를 위한 합성 데이터셋을 생성합니다.

```python
X, y = make_hastie_10_2(n_samples=8000, random_state=42)
```
