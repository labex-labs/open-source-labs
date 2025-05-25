# 객체 지향 프로그래밍 (Object Oriented (OO) programming)

코드가 *객체*들의 모음으로 구성되는 프로그래밍 기법입니다.

*객체*는 다음으로 구성됩니다:

- 데이터. 속성 (Attributes)
- 동작. 객체에 적용되는 함수인 메서드 (Methods)

이 과정에서 이미 일부 객체 지향 프로그래밍을 사용해 왔습니다.

예를 들어, 리스트를 조작하는 경우를 살펴보겠습니다.

```python
>>> nums = [1, 2, 3]
>>> nums.append(4)      # Method
>>> nums.insert(1,10)   # Method
>>> nums
[1, 10, 2, 3, 4]        # Data
>>>
```

`nums`는 리스트의 *인스턴스*입니다.

메서드 (`append()` 및 `insert()`) 는 인스턴스 (`nums`) 에 연결됩니다.
