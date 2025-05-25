# 모듈 찾기

Python 은 모듈을 찾을 때 경로 목록 (sys.path) 을 참조합니다.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
  ...
]
```

현재 작업 디렉토리가 일반적으로 먼저 옵니다.
