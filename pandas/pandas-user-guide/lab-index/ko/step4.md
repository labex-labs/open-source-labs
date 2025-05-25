# 결측 데이터 처리

Pandas 는 데이터를 정리하고 결측값을 채우기 위한 다양한 방법을 제공합니다.

```python
# 결측값을 가진 DataFrame 생성
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# 결측값 채우기
df.fillna(value=0, inplace=True)
```
