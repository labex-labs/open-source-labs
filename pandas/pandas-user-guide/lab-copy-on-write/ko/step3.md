# CoW 를 사용한 체인 할당 이해

이제 CoW 와 함께 체인 할당이 어떻게 작동하는지 이해해 보겠습니다.

```python
# DataFrame 생성
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# CoW 원칙을 위반하는 체인 할당 적용
df["foo"][df["bar"] > 5] = 100

# DataFrame 출력
print(df)
```
