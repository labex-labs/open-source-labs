# Pandas 에서 if/truth 문 사용하기

Pandas 는 모호성 때문에 if/truth 문을 직접 사용하는 것을 지원하지 않습니다. 대신, `.any()`, `.all()`, 또는 `.empty()`와 같은 메서드를 사용하십시오.

```python
# Check if any value in the Series is True
if pd.Series([False, True, False]).any():
    print("At least one True value in the Series")
```
