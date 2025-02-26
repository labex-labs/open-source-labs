# プログラムの終了

プログラムの終了は例外を通じて処理されます。

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

代替案。

```python
import sys
sys.exit(exitcode)
```

ゼロ以外の終了コードはエラーを示します。
