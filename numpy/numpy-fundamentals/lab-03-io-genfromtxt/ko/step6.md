# 변환 조정하기

`converters` 인수를 사용하면 더 복잡한 변환을 처리하기 위한 변환 함수를 정의할 수 있습니다. 열 인덱스 또는 열 이름을 키로, 변환 함수를 값으로 하는 딕셔너리를 허용합니다.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
