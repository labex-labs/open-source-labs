# Emitter 함수 생성

emitter 함수는 update 메서드로 전달될 데이터를 생성합니다. 이 경우, 확률 0.1 로 랜덤 데이터를 생성합니다.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
