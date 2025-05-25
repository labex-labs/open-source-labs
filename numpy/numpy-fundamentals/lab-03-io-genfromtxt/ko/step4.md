# 열 선택하기

`usecols` 인수는 가져올 열을 선택하는 데 사용됩니다. 가져올 열의 인덱스에 해당하는 단일 정수 또는 정수 시퀀스를 허용합니다.

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
