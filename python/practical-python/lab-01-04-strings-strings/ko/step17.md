# 연습 1.18: 정규 표현식 (Regular Expressions)

기본 문자열 연산의 한 가지 제한 사항은 고급 패턴 매칭 (pattern matching) 을 지원하지 않는다는 것입니다. 이를 위해서는 Python 의 `re` 모듈과 정규 표현식을 사용해야 합니다. 정규 표현식 처리는 큰 주제이지만, 다음은 간단한 예입니다.

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Find all occurrences of a date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Replace all occurrences of a date with replacement text
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

`re` 모듈에 대한 자세한 내용은 공식 문서를 참조하십시오: [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
