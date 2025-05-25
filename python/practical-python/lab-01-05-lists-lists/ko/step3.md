# 리스트 반복 및 검색

`for`를 사용하여 리스트 내용을 반복합니다.

```python
for name in names:
    # use name
    # e.g. print(name)
    ...
```

이것은 다른 프로그래밍 언어의 `foreach` 문과 유사합니다.

어떤 항목의 위치를 빠르게 찾으려면 `index()`를 사용합니다.

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

요소가 두 번 이상 존재하면 `index()`는 첫 번째 발생의 인덱스를 반환합니다.

요소를 찾을 수 없으면 `ValueError` 예외가 발생합니다.
