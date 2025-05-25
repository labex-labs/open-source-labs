# 중복 레이블의 결과 이해

중복 레이블은 pandas 에서 특정 작업의 동작을 변경할 수 있습니다. 예를 들어, 일부 메서드는 중복이 있는 경우 작동하지 않습니다.

```python
# Creating a pandas Series with duplicate labels
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Attempting to reindex the Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
