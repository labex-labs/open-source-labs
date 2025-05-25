# DataFrame 을 사용한 CoW 이해

이제 DataFrame 을 생성하고 CoW 가 데이터 수정에 어떤 영향을 미치는지 살펴보겠습니다.

```python
# DataFrame 생성
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# DataFrame 의 하위 집합 생성
subset = df["foo"]

# 하위 집합 수정
subset.iloc[0] = 100

# 원본 DataFrame 출력
print(df)
```

## DataFrame 을 사용한 CoW 구현

이제 DataFrame 을 수정할 때 CoW 를 구현하는 방법을 살펴보겠습니다.

```python
# CoW 활성화
pd.options.mode.copy_on_write = True

# DataFrame 의 하위 집합 생성
subset = df["foo"]

# 하위 집합 수정
subset.iloc[0] = 100

# 원본 DataFrame 출력
print(df)
```
