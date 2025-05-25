# 데이터 정규화

만델브로 집합의 음영 처리 및 거듭제곱 정규화 렌더링을 생성하기 위해 데이터를 정규화해야 합니다. 다음 공식을 사용하여 이를 수행합니다.

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
