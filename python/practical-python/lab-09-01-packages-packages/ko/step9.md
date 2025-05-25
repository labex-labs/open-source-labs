# 스크립트를 위한 또 다른 해결책

앞서 언급했듯이, 이제 패키지 내에서 스크립트를 실행하려면 `-m package.module`을 사용해야 합니다.

```bash
$ python3 -m porty.pcost portfolio.csv
```

또 다른 대안이 있습니다: 새로운 최상위 레벨 스크립트를 작성합니다.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

이 스크립트는 패키지 *외부*에 위치합니다. 예를 들어, 디렉토리 구조를 살펴보면 다음과 같습니다:

    pcost.py       # 최상위 레벨 스크립트 (top-level-script)
    porty/         # 패키지 디렉토리 (package directory)
        __init__.py
        pcost.py
        ...
