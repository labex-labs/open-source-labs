# 환경 변수 (Environment Variables)

환경 변수는 셸에서 설정됩니다.

```bash
$ export NAME dave
$ export RSH ssh
$ python3 prog.py
```

`os.environ`은 이러한 값을 포함하는 딕셔너리입니다.

```python
import os

name = os.environ['NAME'] # 'dave'
```

변경 사항은 프로그램에서 나중에 실행되는 모든 하위 프로세스에 반영됩니다.
