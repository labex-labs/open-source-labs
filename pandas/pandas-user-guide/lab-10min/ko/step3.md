# 데이터프레임 생성

datetime 인덱스와 레이블이 지정된 열을 사용하여 numpy 배열을 전달하여 `DataFrame`을 생성할 수 있습니다.

```python
# pandas dataframe 생성
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
