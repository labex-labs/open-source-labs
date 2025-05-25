# 사용자 정의 함수 (UDF) 메서드를 사용한 변형

UDF 를 사용하는 pandas 메서드를 사용할 때는 UDF 내부에서 DataFrame 을 변경하지 않도록 합니다. 대신, 변경하기 전에 복사본을 만드십시오.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
