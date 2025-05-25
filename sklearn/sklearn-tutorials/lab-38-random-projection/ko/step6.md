# 검증

역변환의 정확성을 검증하기 위해 원본 데이터 `X`를 역변환 결과와 비교할 수 있습니다.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

여기서, 역변환된 데이터 `X_new_inversed`에 변환을 적용하고, `np.allclose` 함수를 사용하여 원래 투영된 데이터 `X_new`와 같은지 확인합니다.
