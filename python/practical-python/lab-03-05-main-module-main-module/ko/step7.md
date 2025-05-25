# 명령줄 인수 (Command Line Args)

명령줄은 텍스트 문자열의 목록입니다.

```bash
$ python3 report.py portfolio.csv prices.csv
```

이 텍스트 문자열 목록은 `sys.argv`에서 찾을 수 있습니다.

```python
# 이전 bash 명령에서
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

다음은 인수를 처리하는 간단한 예시입니다.

```python
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
