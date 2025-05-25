# 결측 데이터 삽입

여기서는 데이터에 결측값을 삽입하는 방법을 살펴보겠습니다.

```python
# Insert missing values
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
