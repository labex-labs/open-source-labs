# 연습 문제 4.11: 사용자 정의 예외 정의

라이브러리가 자체 예외를 정의하는 것은 종종 좋은 관행입니다.

이렇게 하면 일반적인 프로그래밍 오류에 대한 응답으로 발생하는 Python 예외와 특정 사용 문제를 알리기 위해 라이브러리에서 의도적으로 발생하는 예외를 더 쉽게 구별할 수 있습니다.

사용자가 잘못된 형식 이름을 제공할 때 사용자 정의 `FormatError` 예외를 발생시키도록 이전 연습 문제의 `create_formatter()` 함수를 수정하십시오.

예를 들어:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
