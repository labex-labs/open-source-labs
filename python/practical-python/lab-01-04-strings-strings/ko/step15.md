# 연습 1.16: 문자열 메서드 (String Methods)

Python 대화형 프롬프트에서 몇 가지 문자열 메서드를 실험해 보십시오.

```python
>>> symbols.lower()
?
>>> symbols
?
>>>
```

기억하세요, 문자열은 항상 읽기 전용입니다. 연산의 결과를 저장하려면 변수에 저장해야 합니다.

```python
>>> lowersyms = symbols.lower()
>>>
```

몇 가지 더 많은 연산을 시도해 보십시오.

```python
>>> symbols.find('MSFT')
?
>>> symbols[13:17]
?
>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
?
>>> name = '   IBM   \n'
>>> name = name.strip()    # Remove surrounding whitespace
>>> name
?
>>>
```
