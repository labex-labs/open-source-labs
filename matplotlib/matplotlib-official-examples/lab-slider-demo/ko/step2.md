# 사인파 함수 정의

다음으로, 사인파를 생성할 함수를 정의합니다. 이 함수는 진폭과 주파수, 두 개의 매개변수를 입력으로 받아 주어진 시간에 사인파를 반환합니다.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
