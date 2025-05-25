# 문자열 메서드 (String methods)

문자열은 문자열 데이터를 사용하여 다양한 연산을 수행하는 메서드를 가지고 있습니다.

예시: 선행/후행 공백 제거.

```python
s = '  Hello '
t = s.strip()     # 'Hello'
```

예시: 대소문자 변환.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

예시: 텍스트 대체.

```python
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'
```

**더 많은 문자열 메서드:**

문자열은 텍스트 데이터를 테스트하고 조작하기 위한 다양한 메서드를 가지고 있습니다. 다음은 메서드의 작은 예시입니다.

```python
s.endswith(suffix)     # 문자열이 suffix 로 끝나는지 확인
s.find(t)              # s 에서 t 의 첫 번째 발생 위치
s.index(t)             # s 에서 t 의 첫 번째 발생 위치
s.isalpha()            # 문자가 알파벳인지 확인
s.isdigit()            # 문자가 숫자인지 확인
s.islower()            # 문자가 소문자인지 확인
s.isupper()            # 문자가 대문자인지 확인
s.join(slist)          # s 를 구분 기호로 사용하여 문자열 목록을 결합
s.lower()              # 소문자로 변환
s.replace(old,new)     # 텍스트 대체
s.rfind(t)             # 문자열 끝에서부터 t 검색
s.rindex(t)            # 문자열 끝에서부터 t 검색
s.split([delim])       # 문자열을 부분 문자열 목록으로 분할
s.startswith(prefix)   # 문자열이 prefix 로 시작하는지 확인
s.strip()              # 선행/후행 공백 제거
s.upper()              # 대문자로 변환
```
