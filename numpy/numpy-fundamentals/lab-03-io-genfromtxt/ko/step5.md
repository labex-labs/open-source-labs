# 데이터 타입 설정하기

`dtype` 인수는 문자열을 다른 타입으로 변환하는 방식을 제어하는 데 사용됩니다. 단일 타입, 타입 시퀀스, 쉼표로 구분된 문자열, 딕셔너리, 튜플 시퀀스, 기존 `numpy.dtype` 객체 또는 데이터 자체에서 타입을 결정하는 `None`이 될 수 있습니다.

```python
np.genfromtxt(StringIO(data), dtype=float)
```
