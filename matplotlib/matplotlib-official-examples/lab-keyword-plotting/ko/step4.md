# 플롯 생성

이 단계에서는 `data` 딕셔너리를 `scatter()` 함수의 입력으로 사용하여 산점도 (scatter plot) 를 생성합니다. `a`, `b`, `c`, `d` 변수에 해당하는 문자열을 사용하여 플롯을 생성합니다.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
```
