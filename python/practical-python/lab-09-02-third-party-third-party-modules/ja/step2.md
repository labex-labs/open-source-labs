# 標準ライブラリモジュール

Python の標準ライブラリのモジュールは通常、`/usr/local/lib/python3.6` のような場所から来ます。簡単なテストを行うことで確認できます。

```python
>>> import re
>>> re
<module 're' from '/usr/local/lib/python3.6/re.py'>
>>>
```

REPL でモジュールを見るだけでも、そのファイルの場所がわかるので、便利なデバッグヒントになります。
