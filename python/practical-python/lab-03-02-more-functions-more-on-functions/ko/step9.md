# 전역 변수 (Global Variables)

함수는 동일한 파일에 정의된 전역 변수의 값에 자유롭게 접근할 수 있습니다.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Using `name` global variable
```

하지만, 함수는 전역 변수를 수정할 수 없습니다:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # prints 'Dave'
```

**기억하세요: 함수 내의 모든 할당은 지역적입니다.**
