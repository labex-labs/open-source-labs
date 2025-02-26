# REPL の使用方法

スクリプトを実行する際に、オプション `-i` を使って Python を実行中に維持します。

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>
```

これによりインタプリタの状態が保持されます。つまり、クラッシュ後に調べることができます。変数の値やその他の状態を確認できます。
