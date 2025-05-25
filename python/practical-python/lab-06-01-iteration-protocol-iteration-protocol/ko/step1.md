# 어디에나 있는 반복 (Iteration Everywhere)

다양한 객체가 반복을 지원합니다.

```python
a = 'hello'
for c in a: # a 의 문자들을 순회합니다 (Loop over characters in a)
    ...

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # 딕셔너리의 키들을 순회합니다 (Loop over keys in dictionary)
    ...

c = [1,2,3,4]
for i in c: # 리스트/튜플의 항목들을 순회합니다 (Loop over items in a list/tuple)
    ...

f = open('foo.txt')
for x in f: # 파일의 라인들을 순회합니다 (Loop over lines in a file)
    ...
```
