# 연습 문제 2.14: 더 많은 시퀀스 연산 (More sequence operations)

몇 가지 시퀀스 축소 연산 (sequence reduction operations) 을 대화형으로 실험해 보세요.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

데이터를 반복 (looping) 해 보세요.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

때때로 `for` 문, `len()`, 그리고 `range()`는 초보자에 의해 녹슨 C 프로그램의 심연에서 튀어나온 듯한 끔찍한 코드 조각으로 사용됩니다.

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

그렇게 하지 마세요! 그렇게 읽는 것은 모두의 눈을 아프게 할 뿐만 아니라, 메모리 측면에서 비효율적이며 훨씬 느리게 실행됩니다. 데이터를 반복하고 싶다면 일반적인 `for` 루프를 사용하세요. 어떤 이유로 인덱스 (index) 가 필요한 경우 `enumerate()`를 사용하세요.
