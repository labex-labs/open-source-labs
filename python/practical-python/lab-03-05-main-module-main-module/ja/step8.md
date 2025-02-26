# 標準入出力

標準入出力（またはstdio）は、通常のファイルと同じように機能するファイルです。

```python
sys.stdout
sys.stderr
sys.stdin
```

デフォルトでは、printは`sys.stdout`に出力されます。入力は`sys.stdin`から読み取られます。トレースバックとエラーは`sys.stderr`に出力されます。

stdioは、端末、ファイル、パイプなどに接続されている可能性があることに注意してください。

```bash
$ python3 prog.py > results.txt
# または
$ cmd1 | python3 prog.py | cmd2
```
