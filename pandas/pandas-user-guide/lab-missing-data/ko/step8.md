# 결측값을 나타내는 NA 스칼라 이해

마지막으로, 결측값을 나타내는 데 사용할 수 있는 pandas 의 실험적인 `NA` 스칼라에 대해 논의하겠습니다.

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
