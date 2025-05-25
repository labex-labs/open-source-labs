# 문제점: 메인 스크립트 (Main Scripts)

패키지 서브모듈을 메인 스크립트로 실행하면 작동하지 않습니다.

```bash
$ python porty/pcost.py # BREAKS
...
```

_이유: 단일 파일에서 Python 을 실행하고 있으며, Python 은 나머지 패키지 구조를 올바르게 인식하지 못합니다 (`sys.path`가 잘못되었습니다)._

모든 import 가 깨집니다. 이를 해결하려면 `-m` 옵션을 사용하여 프로그램을 다른 방식으로 실행해야 합니다.

```bash
$ python -m porty.pcost # WORKS
...
```
