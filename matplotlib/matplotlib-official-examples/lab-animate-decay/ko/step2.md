# 데이터 생성기 함수 생성

다음으로, 애니메이션에 대한 데이터를 생성하는 함수를 만들어야 합니다. 이 함수는 시간이 지남에 따라 감쇠하는 사인파를 생성합니다. `itertools.count()` 함수를 사용하여 무한 시퀀스의 숫자를 생성합니다. 이 숫자들을 사용하여 사인파의 값을 계산합니다.

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
