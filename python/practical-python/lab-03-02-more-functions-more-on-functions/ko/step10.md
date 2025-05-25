# 전역 변수 수정 (Modifying Globals)

전역 변수를 수정해야 하는 경우, 해당 변수를 전역 변수로 선언해야 합니다.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Changes the global name above
```

`global` 선언은 사용 전에 나타나야 하며, 해당 변수는 함수와 동일한 파일에 존재해야 합니다. 이를 알았으니, 이는 좋지 않은 형식으로 간주된다는 것을 알아두세요. 사실, 가능하다면 `global`을 완전히 피하도록 노력하세요. 함수가 함수 외부의 어떤 종류의 상태를 수정해야 하는 경우, 대신 클래스를 사용하는 것이 더 좋습니다 (이에 대한 자세한 내용은 나중에 다룹니다).
