# 할당 (Assignment)

Python 의 많은 연산은 값을 *할당*하거나 *저장*하는 것과 관련이 있습니다.

```python
a = value         # Assignment to a variable
s[n] = value      # Assignment to a list
s.append(value)   # Appending to a list
d['key'] = value  # Adding to a dictionary
```

_주의 사항: 할당 연산은 **절대로** 할당되는 값의 복사본을 만들지 않습니다._ 모든 할당은 단순히 참조 복사 (또는 선호하는 경우 포인터 복사) 입니다.
