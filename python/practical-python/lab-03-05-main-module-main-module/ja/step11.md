# `#!` 行

Unix では、`#!` 行を使ってスクリプトを Python として起動できます。スクリプトファイルの最初の行に次のように追加します。

```python
#!/usr/bin/env python3
#./prog.py
...
```

実行可能なパーミッションが必要です。

```bash
$ chmod +x prog.py
# その後、実行できます
$./prog.py
... 出力...
```

_注：Windows の Python ランチャーも、言語バージョンを示すために `#!` 行を探します。_
