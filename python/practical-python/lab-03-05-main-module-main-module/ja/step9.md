# 環境変数

環境変数はシェルで設定されます。

```bash
$ export NAME=dave
$ export RSH=ssh
$ python3 prog.py
```

`os.environ` はこれらの値を含む辞書です。

```python
import os

name = os.environ['NAME'] # 'dave'
```

変更は、プログラムによって後で起動されるサブプロセスに反映されます。
