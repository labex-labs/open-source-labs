# 변수 범위 (Variable Scope)

프로그램은 변수에 값을 할당합니다.

```python
x = value # 전역 변수 (Global variable)

def foo():
    y = value # 지역 변수 (Local variable)
```

변수 할당은 함수 정의 외부와 내부에서 발생합니다. 외부에서 정의된 변수는 "전역 (global)" 변수입니다. 함수 내의 변수는 "지역 (local)" 변수입니다.
