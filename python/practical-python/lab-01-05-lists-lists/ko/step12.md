# 연습 문제 1.24: 모든 것을 다시 합치기

문자열 리스트를 가져와서 하나의 문자열로 결합하고 싶으십니까? 다음과 같이 문자열의 `join()` 메서드를 사용하십시오 (참고: 처음에는 이상하게 보일 수 있습니다).

```python
>>> a = ','.join(symlist)
>>> a
'YHOO,RHT,HPQ,GOOG,AIG,AAPL,AA'
>>> b = ':'.join(symlist)
>>> b
'YHOO:RHT:HPQ:GOOG:AIG:AAPL:AA'
>>> c = ''.join(symlist)
>>> c
'YHOORHTHPQGOOGAIGAAPLAA'
>>>
```
