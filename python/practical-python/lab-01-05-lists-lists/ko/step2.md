# 리스트 연산

리스트는 모든 유형의 항목을 저장할 수 있습니다. `append()`를 사용하여 새 항목을 추가합니다.

```python
names.append('Murphy')    # 끝에 추가 (Adds at end)
names.insert(2, 'Aretha') # 중간에 삽입 (Inserts in middle)
```

`+`를 사용하여 리스트를 연결합니다.

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

리스트는 정수로 인덱싱됩니다. 0 부터 시작합니다.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

음수 인덱스는 끝에서부터 계산합니다.

```python
names[-1] # 'Curtis'
```

리스트의 모든 항목을 변경할 수 있습니다.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

리스트의 길이.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

멤버십 테스트 (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

복제 (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
