# `#!` 라인 (line)

Unix 시스템에서 `#!` 라인은 스크립트를 Python 으로 실행할 수 있게 합니다. 스크립트 파일의 첫 번째 줄에 다음을 추가하십시오.

```python
#!/usr/bin/env python3
#./prog.py
...
```

실행 권한이 필요합니다.

```bash
$ chmod +x prog.py
# 그런 다음 실행할 수 있습니다.
$ ./prog.py
... output ...
```

_참고: Windows 의 Python Launcher 도 언어 버전을 나타내기 위해 `#!` 라인을 찾습니다._
