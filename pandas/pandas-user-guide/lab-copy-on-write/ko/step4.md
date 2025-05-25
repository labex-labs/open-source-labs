# CoW 를 사용한 체인 할당 구현

마지막으로, `loc` 메서드를 사용하여 CoW 와 함께 체인 할당을 구현하는 방법을 살펴보겠습니다.

```python
# DataFrame 생성
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# 'loc'을 사용하여 CoW 와 함께 체인 할당 적용
df.loc[df["bar"] > 5, "foo"] = 100

# DataFrame 출력
print(df)
```
