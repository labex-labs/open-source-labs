# 연습 문제 7.1: 가변 인자의 간단한 예시

다음 함수를 정의해 보세요:

```python
>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
```

`*more` 매개변수가 어떻게 모든 추가 인자를 수집하는지 확인하세요.
