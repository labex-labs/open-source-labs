# 연습 문제 6.14: 함수 인자 (Function Arguments) 에서의 제너레이터 표현식

제너레이터 표현식은 때때로 함수 인자에 배치됩니다. 처음에는 약간 이상해 보일 수 있지만, 다음 실험을 시도해 보십시오:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # A list comprehension
55
>>> sum(x*x for x in nums)      # A generator expression
55
>>>
```

위의 예에서, 제너레이터를 사용하는 두 번째 버전은 큰 리스트를 조작하는 경우 메모리를 훨씬 적게 사용합니다.

`portfolio.py` 파일에서 리스트 컴프리헨션을 포함하는 몇 가지 계산을 수행했습니다. 이를 제너레이터 표현식으로 바꿔보십시오.
