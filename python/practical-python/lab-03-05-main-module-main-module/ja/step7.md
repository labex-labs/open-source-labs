# コマンドライン引数

コマンドラインは、文字列のリストです。

```bash
$ python3 report.py portfolio.csv prices.csv
```

この文字列のリストは、`sys.argv` の中にあります。

```python
# 前の bash コマンドで
sys.argv # ['report.py', 'portfolio.csv', 'prices.csv']
```

引数を処理する簡単な例を以下に示します。

```python
import sys

if len(sys.argv)!= 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
