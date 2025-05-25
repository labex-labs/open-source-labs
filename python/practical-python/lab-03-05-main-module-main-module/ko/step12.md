# 스크립트 템플릿 (Script Template)

마지막으로, 명령줄 스크립트로 실행되는 Python 프로그램에 대한 일반적인 코드 템플릿은 다음과 같습니다.

```python
#!/usr/bin/env python3
#./prog.py

# Import statements (라이브러리)
import modules

# Functions
def spam():
    ...

def blah():
    ...

# Main function
def main(argv):
    # Parse command line args, environment, etc.
    ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```
