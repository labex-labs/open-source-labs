# 행을 열로 분할하기

`delimiter` 인수는 행을 열로 분할하는 방법을 정의하는 데 사용됩니다. 기본적으로 `numpy.genfromtxt`는 `delimiter=None`을 가정하며, 이는 행이 공백 (탭 포함) 을 기준으로 분할됨을 의미합니다.

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
