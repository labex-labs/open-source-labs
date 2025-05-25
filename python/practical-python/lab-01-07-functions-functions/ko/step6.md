# 연습 문제 1.29: 함수 정의하기 (Defining a function)

간단한 함수를 정의해 보십시오:

```python
>>> def greeting(name):
        'Issues a greeting'
        print('Hello', name)

>>> greeting('Guido')
Hello Guido
>>> greeting('Paula')
Hello Paula
>>>
```

함수의 첫 번째 문이 문자열인 경우, 이는 문서로 사용됩니다. `help(greeting)`과 같은 명령을 입력하여 표시되는 내용을 확인해 보십시오.
