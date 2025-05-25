# 연습 문제 3.8: 예외 발생시키기

이전 섹션에서 작성한 `parse_csv()` 함수는 사용자가 지정한 열을 선택할 수 있도록 하지만, 이는 입력 데이터 파일에 열 헤더가 있는 경우에만 작동합니다.

`select` 및 `has_headers=False` 인수가 모두 전달되면 예외가 발생하도록 코드를 수정하십시오. 예를 들어:

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

이 검사를 추가한 후, 함수에서 다른 종류의 유효성 검사를 수행해야 하는지 질문할 수 있습니다. 예를 들어, 파일 이름이 문자열인지, types 가 리스트인지 또는 이와 유사한 사항을 확인해야 할까요?

일반적으로, 이러한 검사를 건너뛰고 잘못된 입력에 대해 프로그램이 실패하도록 하는 것이 가장 좋습니다. 트레이스백 메시지는 문제의 원인을 지적하고 디버깅을 돕습니다.

위의 검사를 추가하는 주된 이유는 비논리적인 모드에서 코드를 실행하는 것을 방지하기 위함입니다 (예: 열 헤더가 필요한 기능을 사용하면서 동시에 헤더가 없다고 지정하는 경우).

이는 호출 코드 측의 프로그래밍 오류를 나타냅니다. "발생하지 않아야 하는" 경우를 확인하는 것은 종종 좋은 생각입니다.
