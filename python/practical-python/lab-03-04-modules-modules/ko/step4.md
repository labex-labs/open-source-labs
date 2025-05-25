# 환경으로서의 모듈 (Modules as Environments)

모듈은 내부에 정의된 모든 코드에 대한 묶는 환경을 형성합니다.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

_전역_ 변수는 항상 묶는 모듈 (동일한 파일) 에 바인딩됩니다. 각 소스 파일은 자체적인 작은 우주입니다.
