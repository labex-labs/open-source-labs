# 제너레이터 파이프라인

제너레이터의 이러한 측면을 사용하여 (Unix 파이프와 같은) 처리 파이프라인을 설정할 수 있습니다.

_생산자_(producer) → _처리_(processing) → _처리_(processing) → _소비자_(consumer)

처리 파이프는 초기 데이터 생산자, 일부 중간 처리 단계 집합 및 최종 소비자를 갖습니다.

**생산자**(producer) → _처리_(processing) → _처리_(processing) → _소비자_(consumer)

```python
def producer():
    ...
    yield item
    ...
```

생산자는 일반적으로 제너레이터입니다. 다른 시퀀스의 목록일 수도 있습니다. `yield`는 파이프라인에 데이터를 공급합니다.

_생산자_(producer) → _처리_(processing) → _처리_(processing) → **소비자**(consumer)

```python
def consumer(s):
    for item in s:
        ...
```

소비자는 for-loop 입니다. 항목을 가져와서 무언가를 수행합니다.

_생산자_(producer) → **처리**(processing) → **처리**(processing) → _소비자_(consumer)

```python
def processing(s):
    for item in s:
        ...
        yield newitem
        ...
```

중간 처리 단계는 동시에 항목을 소비하고 생성합니다. 데이터 스트림을 수정할 수 있습니다. 또한 필터링 (항목 폐기) 할 수도 있습니다.

_생산자_(producer) → _처리_(processing) → _처리_(processing) → _소비자_(consumer)

```python
def producer():
    ...
    yield item          # yields the item that is received by the `processing`
    ...

def processing(s):
    for item in s:      # Comes from the `producer`
        ...
        yield newitem   # yields a new item
        ...

def consumer(s):
    for item in s:      # Comes from the `processing`
        ...
```

파이프라인을 설정하는 코드

```python
a = producer()
b = processing(a)
c = consumer(b)
```

데이터가 다른 함수를 통해 점진적으로 흐르는 것을 알 수 있습니다.

이 연습을 위해 `stocksim.py` 프로그램이 백그라운드에서 계속 실행되어야 합니다. 이전 연습에서 작성한 `follow()` 함수를 사용합니다.
