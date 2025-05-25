# 결측 데이터를 사용한 계산 수행

결측 데이터를 사용하여 기본적인 산술 및 통계 계산을 수행합니다.

```python
# Perform calculations with missing data
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```
