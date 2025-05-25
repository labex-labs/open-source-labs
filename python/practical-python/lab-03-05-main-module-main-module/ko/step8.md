# 표준 I/O (Standard I/O)

표준 입력/출력 (Standard Input / Output, 또는 stdio) 은 일반 파일과 동일하게 작동하는 파일입니다.

```python
sys.stdout
sys.stderr
sys.stdin
```

기본적으로 `print`는 `sys.stdout`으로 향합니다. 입력은 `sys.stdin`에서 읽습니다. Traceback 및 오류는 `sys.stderr`으로 향합니다.

*stdio*는 터미널, 파일, 파이프 등에 연결될 수 있다는 점에 유의하십시오.

```bash
$ python3 prog.py > results.txt
# or
$ cmd1 | python3 prog.py | cmd2
```
