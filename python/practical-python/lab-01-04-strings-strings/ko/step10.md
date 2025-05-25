# Raw 문자열 (Raw Strings)

Raw 문자열은 해석되지 않은 백슬래시를 가진 문자열 리터럴입니다. 소문자 "r"로 초기 따옴표를 접두사로 지정하여 정의합니다.

```python
>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'
```

문자열은 입력한 그대로, 안에 묶인 리터럴 텍스트입니다. 이는 백슬래시가 특별한 의미를 갖는 상황에서 유용합니다. 예: 파일 이름, 정규 표현식 등.
