# 연습 1.14: 문자열 연결 (String concatenation)

문자열 데이터는 읽기 전용이지만, 항상 변수를 새로 생성된 문자열에 다시 할당할 수 있습니다.

새로운 기호 "GOOG"을 `symbols`의 끝에 연결하는 다음 문장을 시도해 보십시오.

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

이런! 원하는 결과가 아닙니다. `symbols` 변수가 값 `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`를 갖도록 수정하십시오.

```python
>>> symbols = ?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

문자열 앞에 `'HPQ'`를 추가하십시오.

```python
>>> symbols = ?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

이 예제에서는 문자열이 읽기 전용이라는 것을 위반하는 것처럼 보일 수 있지만, 원래 문자열이 수정되는 것처럼 보일 수 있습니다. 그렇지 않습니다. 문자열에 대한 연산은 매번 완전히 새로운 문자열을 생성합니다. 변수 이름 `symbols`가 다시 할당되면 새로 생성된 문자열을 가리킵니다. 그 후, 이전 문자열은 더 이상 사용되지 않으므로 파괴됩니다.
