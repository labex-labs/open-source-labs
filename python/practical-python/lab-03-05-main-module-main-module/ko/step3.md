# `__main__` 확인 (check)

메인 스크립트로 실행되는 모듈은 다음 관례를 사용하는 것이 일반적입니다.

```python
# prog.py
...
if __name__ == '__main__':
    # Running as the main program ...
    statements
    ...
```

`if` 문 안에 포함된 문장이 _main_ 프로그램이 됩니다.
