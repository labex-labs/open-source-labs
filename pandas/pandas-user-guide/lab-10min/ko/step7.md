# 결측 데이터 처리

Pandas 는 데이터프레임에서 결측 데이터를 처리하는 메서드를 제공합니다.

```python
# 결측 데이터 채우기
df.fillna(value=5)

# 값이 nan 인 위치의 boolean 마스크 얻기
pd.isna(df)
```
