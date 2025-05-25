# 단축 함수 사용하기

`numpy.lib.npyio` 모듈은 `numpy.genfromtxt`에서 파생된 단축 함수를 제공합니다. 이러한 함수는 서로 다른 기본값을 가지며 표준 NumPy 배열 또는 마스크된 배열을 반환합니다.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
