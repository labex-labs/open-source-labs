# 프로그램 종료 (Program Exit)

프로그램 종료는 예외 (exceptions) 를 통해 처리됩니다.

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

다른 방법:

```python
import sys
sys.exit(exitcode)
```

0 이 아닌 종료 코드 (exit code) 는 오류를 나타냅니다.
